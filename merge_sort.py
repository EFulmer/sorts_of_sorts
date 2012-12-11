# Standard merge sort, done in Python as an exercise.
# TODO: take number argument, sort that many numbers, and fail gracefully.

from math import floor
from random import shuffle
from sys import argv

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = floor(len(list)/2)
    left = merge_sort(list[0:mid])
    right = merge_sort(list[mid:])
    return merge(left, right)

def merge(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j = j + 1
    if i < len(a):
        c.extend(a[i:])
    else:
        c.extend(b[j:])
    return c

def main():
    print('Hello')
    list = [x for x in range(10)]
    shuffle(list)
    print('Input:', list)
    list = merge_sort(list)
    print('Output:', list)

if __name__ == 'main':
    main()
