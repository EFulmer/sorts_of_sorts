
from random import shuffle

def insertion_sort(l):
    for i in range(len(l)-1):
        j = i
        while j > -1:
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
            j = j-1

def main():
    print 'Test of insertion sort:'
    lst = [x for x in range(10)]
    shuffle(lst)
    print 'Unsorted:', lst
    insertion_sort(lst)
    print 'Sorted:', lst

if __name__ == '__main__':
    main()
