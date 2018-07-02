# Solution to Python problem 72

## Solution code
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Counting fractions
Problem 72
Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, ...
... 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions
for d ≤ 1,000,000?
"""
from sys import version_info

if version_info.major > 2:
    range = range


def countingfracs(lim=8):
    phi_dictionary = {i: i for i in range(1, lim + 1)}

    for n in range(2, lim + 1):
        if n == phi_dictionary[n]:
            for nnn in range(n, lim + 1, n):
                phi_dictionary[nnn] -= (phi_dictionary[nnn] / n)
    return sum(v for k, v in phi_dictionary.items()) - 1


def p072():
    return countingfracs(10 ** 6)


if __name__ == '__main__':
    assert 21 == countingfracs()
    sol = p072()
    print("# elements in the set of reduced proper fracs: {}".format(sol))
```

## Home made solution dependencies