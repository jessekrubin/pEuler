#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
# Done"""The Fibonacci sequence is defined by the recurrence relation:

"""
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to
contain 1000 digits?
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def n_b_ten_digits(n):
    digs = sum((1 for i in str(n)))
    return(digs)

def ind_first_fib_w_n_digs(n):
    n_fib_digs = 0
    i = 0
    while(n_fib_digs < n):
        n_fib_digs=n_b_ten_digits(fib(i))
        i += 1
    return(i - 1)

n = 3
answer = ind_first_fib_w_n_digs(n)
print("index of first fib num w/ {} digits: {}".format(n, answer))

n = 1000
answer = ind_first_fib_w_n_digs(n)
print("index of first fib num w/ {} digits: {}".format(n, answer))
