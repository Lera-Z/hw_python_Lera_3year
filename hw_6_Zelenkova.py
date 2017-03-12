import re
import pandas as pd
import unittest

with open('snippets.txt', 'r') as f:
    f = f.read()

def to_table_pandas(left, word, right):
    """ create a DataFrame object with three columns: left context, word, right context
    :param left: list - array with all left contexts
    :param word: str - keyword
    :param right: list - array with all right contexts
    :return: Pandas DataFrame - table of snippets

    """
    table = pd.DataFrame(columns=['left_cont', 'word', 'right_cont'])
    for row1, row2 in zip(left, right):
        table.loc[len(table)] = [' '.join(row1), word, ' '.join(row2)]
    return table

def to_table_simple(left, word, right, max_left):
    """ create simple table from contexts using 'format' methods

    :param left: list - array with all left contexts
    :param word: str - keyword
    :param right: list - array with all right contexts
    :param max_left: int - maximum length of left context
    :return: array - table of snippets

    """
    table_arr = []
    len_word = len(word)
    for row1, row2 in zip(left, right):
        row = '{:>{max_left}}   {:^{len_word}}   {}'.format(' '.join(row1), word, ' '.join(row2), max_left = max_left, len_word = len_word)
        table_arr.append(row)
    table = '\n'.join(table_arr)
    return table

def kwiq(word, text, num=3):
    """ create snippets with a given keyword

    :param word: str - keyword
    :param text: string - text to look for snippets
    :param num: - int - length of left and right contexts of snippets
    :return: Pandas DataFrame or array - table of snippets
    """
    snippets = []
    array_text = text.split()
    if num == 0:
        raise ValueError('num = 0. Are you sure you wanted zero contexts')
    if word not in text:
        raise ValueError('no such word in text')
    indeces = [i for i, val in enumerate(array_text) if re.match(word, val)]
    left = []
    right = []
    max_left = 0
    for ind in indeces:
        if (ind >= num) and (ind <= len(array_text)-(num+1)):
            left_cont = array_text[(ind-num):ind]
            if max_left < len(' '.join(left_cont)):
                max_left = len(' '.join(left_cont))
            left.append(left_cont)
            right_cont = array_text[(ind+1):(ind+num+1)]
            right.append(right_cont)
            snippets.append(' '.join(left_cont + [word] + right_cont))
        elif (ind < num) and (ind <= len(array_text)-(num+1)): # то есть у слова недостаточно контекста слева
            left_cont = array_text[:ind]
            if max_left < len(' '.join(left_cont)):
                max_left = len(' '.join(left_cont))
            left.append(left_cont)
            right_cont = array_text[(ind+1):(ind+num+1)]
            right.append(right_cont)
            snippets.append(' '.join(left_cont + [word] + right_cont))
        elif (ind >= num) and (ind > len(array_text)-(num+1)):  # недостаточно контекста справа
            left_cont = array_text[(ind-num):ind]
            if max_left < len(' '.join(left_cont)):
                max_left = len(' '.join(left_cont))
            left.append(left_cont)
            right_cont = array_text[(ind+1):(len(text)-1)]
            right.append(right_cont)
            snippets.append(' '.join(left_cont + [word] + right_cont))
        elif (ind < num) and (ind >= len(array_text)-(num+1)):
            left_cont = array_text[:ind]
            right_cont = array_text[(ind + 1):(len(text) - 1)]
            right.append(right_cont)
            left.append(left_cont)
    table = to_table_simple(left, word, right, max_left)
    return table

class test_kwiq_TestCase(unittest.TestCase):
    """
    class for testing
    """
    def test_shortest_text(self):
        self.assertEqual(('   word   '), kwiq('word', 'word'))
    def test_no_word_in_txt(self):
        with self.assertRaises(ValueError):
            kwiq('apple', 'banana mango')
    def test_num_is_zero(self):
        with self.assertRaises(ValueError):
            kwiq('apple', 'I love apples', num=0)


print(kwiq('cool', 'I can write tests cool so useful such wow', num=6))

if __name__ == "__main__":
    unittest.main()
