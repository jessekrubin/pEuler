# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Triangular, pentagonal, and hexagonal
Problem 45
Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3,  6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""


def tn(n):
    return int(n * ((n + 1) / 2))


def pn(n):
    return int(n * (((3 * n) - 1) / 2))


def hn(n):
    return int(n * ((2 * n) - 1))


def p045():
    p_nums = []
    h_nums = []
    all_three = []

    i = 1
    while len(all_three) < 3:
        t = tn(i)
        p_nums.append(pn(i))
        h_nums.append(hn(i))
        if t in p_nums:
            if t in h_nums:
                # print(t)
                all_three.append(t)
        i += 1

    return all_three[2]


if __name__ == '__main__':
    answer = p045()
    print("Next #: {}".format(answer))