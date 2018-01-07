# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

"""
Highly divisible triangular number
Problem 12

The sequence of triangle numbers is generated by adding the natural numbers. So
the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten
terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1, 3
 6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28

We can see that 28 is the first triangle number to have over five divisors_gen.

What is the value of the first triangle number to have over five hundred
divisors_gen?
"""

from helpme import n_divisors

cur_triangle_number = 1
maxmax = 1
i = 1
while maxmax < 500:
    i += 1
    cur_triangle_number += i
    numDivs = n_divisors(cur_triangle_number)
    if numDivs > maxmax:
        maxmax = numDivs

print(f"tri num index: {i}")
print(f"triangle #: {cur_triangle_number}")
print(f"# divisors_gen: {n_divisors(cur_triangle_number)}")
# tri num index: 12375
# cur #: 76576500
# # divisors_gen: 576
