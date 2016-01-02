import random

def partition(items, first,last):
    pivot = first + random.randrange(last - first + 1)
    swap(items, pivot, last)
    for i in range(first,last):
        if items[i]<= items[last]:
            swap(items, i , first)
            first = first + 1
    swap(items, first, last)
    return first



def swap(A, x, y):
    A[x], A[y] = A[y], A[x]




def quick_sort(items, first, last):
    if first < last:
        p = partition(items, first,last)
        quick_sort(items, first, p-1)
        quick_sort(items, p + 1, last)
    return items

def main():
    items = [5,4,9,8,1,2]
    n = len(items)
    items = quick_sort(items, 0 , n-1)
    print(items)

main()



