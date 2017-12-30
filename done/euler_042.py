# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

"""
Coded triangle numbers
Problem 42
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle words?
"""

#open file and put into list
with open(r'text_files/words_p42.txt', 'r') as f:
    words = [s.strip("\"") for s in f.readlines()[0].split(',')]


def string_score(name):
    # print(name)
    name = name.lower()
    score = 0
    for character in name:
        score += (ord(character)-96)
    return (score)

word_scores = map(string_score, words)
max_word_score = (max(map(string_score, words)))

i = 2
cur_triangle_num = 1
triangle_numbers_below_max = []
while(cur_triangle_num <= max_word_score):
    triangle_numbers_below_max.append(cur_triangle_num)
    cur_triangle_num += i
    i += 1

total =sum([1 for i in word_scores if i in triangle_numbers_below_max])
print("# coded triangle numbers: {}".format(total))