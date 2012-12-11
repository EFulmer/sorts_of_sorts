
from random import shuffle

def insertion_sort(l):
    for i in range(len(l)-1):
        j = i
        while j > -1:
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
            j = j-1

def main():
    list = [1,2,3,4,5,6,7]
    shuffle(list)
    print('Unsorted:', list)
    insertion_sort(list)
    print('Sorted:', list)

if __name__ == '__main__':
    main()
