#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

import itertools


def find_max(a, b, c):
    max_values = zip(a,b,c)
    max_sum = []
    for i in max_values:
        max_sum.append(sum(i))

    max_v = 0
    index = 0
    for i, v in enumerate(max_sum):
        if v > max_v:
            max_v = v
            index = i
    return index

def get_a_vector(m, index):
    iter = 0
    for i in m:
        for j in i:
            if iter == index:
                return j
            iter += 1

def get_b_vector(m, index ):
    b = []
    decim = 10 * index / 10
    iter = 0
    k = 0
    for i in m:
        for j in i:
            if iter >= decim:
                b.append(j[index%10])
                k += 1
            if k == 10:
                return b
            iter += 1

def get_c_vector(m, index, z):
    c = []
    k = index / 10
    for j in z[k]:
        c.append(j[index%10])
    return c

def solve(m):
    """

    :param m: 3-d matrix
    :return: 3 lists of orthogonal vectors
    """
    a_sum = []
    b_sum = []
    c_sum = []
    p = 0
    z = {}
    for i in range(10):
        z[i] = []
    for i in m:
        b = list(i[0])
        # sum up rows
        for j in i:
            print j
            a_sum.append(sum(j))
            if p != 0:
                for k in range(10):
                    b[k] += j[k]
            p += 1
        print ""
        p = 0
        # sum up columns
        b_sum.append(b)
        # form z-axis
        for j in i:
            r = z[p]
            r.append(j)
            z[p] = r
            p += 1
        p = 0

    # sum up z-axis
    for k in z.keys():
        c = list(z[k][0])
        for j in z[k]:
            if p != 0:
                for u in range(10):
                        c[u] += j[u]
            p += 1
        c_sum.append(c)

    b_sum = list(itertools.chain(*b_sum))
    c_sum = list(itertools.chain(*c_sum))
    print a_sum
    print b_sum
    print c_sum
    index = find_max(a_sum, b_sum, c_sum)
    print index
    a_vector = get_a_vector(m, index)
    b_vector = get_b_vector(m, index)
    c_vector = get_c_vector(m, index, z)
    print (sum(a_vector), sum(b_vector), sum(c_vector))
    return (a_vector, b_vector, c_vector)

def generate_matrix():
    random.seed(1)
    return [[[random.randrange(0,10) for k in range(10)] for j in range(10)] for i in range(10)]


def main():
    m = generate_matrix()
    a, b, c = solve(m)
    print a, b, c


if __name__ == "__main__":
    main()