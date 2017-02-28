import json

with open('python_mystem.json', 'r') as f:
    text = f.readlines()

class Word:
    def __init__(self, wordform, *values, **kvalues):
        self.wordform = wordform
        self.analyses = values
        vars(self).update(kvalues)

def add_word_to_class(line):
    line_json = json.loads(line)
    wordform = line_json['text']
    analyses = line_json.get('analysis')
    if analyses:
        n_of_analyses = len(analyses)
        gr_str = analyses[0]['gr']
        gr_str_half = gr_str.split('=')[0]
        freq_pos = gr_str_half.split(',')[0]
        freq_lemma = analyses[0]['lex']
        gr_str_all = [analyses[i]['gr'] for i in range(len(analyses)-1)]
        word = Word(wordform, *gr_str_all, n_of_analyses=n_of_analyses, freq_pos=freq_pos, freq_lemma=freq_lemma)
    else:
        word = Word(wordform)
    return word


all_words = []
for line in text:
    word = add_word_to_class(line)
    all_words.append(word)

'''
в all_words добавляются все токены подряд, в т.ч. пробелы
'''