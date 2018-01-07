#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

NUMBER = 10
ANSWER = sum([i + 1 for i in range(NUMBER)]) ** 2 - sum([(i + 1) ** 2 for i in range(NUMBER)])
print("Difference ({}): {}".format(NUMBER, ANSWER))

NUMBER = 100
ANSWER = sum([i + 1 for i in range(NUMBER)]) ** 2 - sum([(i + 1) ** 2 for i in range(NUMBER)])
print("Difference ({}): {}".format(NUMBER, ANSWER))
