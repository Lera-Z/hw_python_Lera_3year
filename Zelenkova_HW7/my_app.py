import datetime

from flask import Flask
from flask import url_for, render_template, request, redirect
from collections import defaultdict

app = Flask(__name__)

stat = {'cats':[], 'dogs':[]}
people = defaultdict(int)


@app.route('/')
def index():
    if request.args:
        name = request.args['name']
        people[name] += 1
        cats = True if 'cats' in request.args else False
        dogs = True if 'dogs' in request.args else False
        if cats:
            stat['cats'].append(name)
        if dogs:
            stat['dogs'].append(name)
        len_cats = len(stat['cats'])
        len_dogs = len(stat['dogs'])
        return render_template('answer.html', stat=stat, people=people, name=name,
                               len_dogs=len_dogs, len_cats=len_cats)
    return render_template('question.html')


@app.route('/hi')
@app.route('/hi/<user>')
def hi(user=None):
    if user is None:
        user = 'friend'
    return '<html><body><p>Привет, ' + user + '!</p></body></html>'


@app.route('/form')
def form():
    if request.args:
        name = request.args['name']
        age = request.args['age']
        st = True if 'student' in request.args else False
        return render_template('answer.html', name=name, age=age, student=st)
    return render_template('question.html')


@app.route('/thanks')
def thanks():
    if request.args:
        name = request.args['name']
        book = request.args['book']
        return render_template('thanks.html', name=name, book=book)
    return redirect(url_for('books'))


@app.route('/time')
def time_redirect():
    h = datetime.datetime.today().hour
    if 10 < h < 18:
        return redirect(url_for('index'))
    return redirect(url_for('hi'))


if __name__ == '__main__':
    app.run(debug=True)