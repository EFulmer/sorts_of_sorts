# Standard merge sort, done in Python as an exercise.

from math import floor
from random import shuffle

def merge_sort(ls):
    if len(ls) <= 1:
        return ls
    # in smaller arrays, it'd be better to do insertion sort to reduce overhead
    mid = int(floor(len(ls)/2))
    left = merge_sort(ls[0:mid])
    right = merge_sort(ls[mid:])
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
    print 'Test of merge sort:'
    lst = [x for x in range(10)]
    shuffle(lst)
    print 'Input:', lst
    lst = merge_sort(lst)
    print 'Output:', lst

if __name__ == '__main__':
    main()
