def bubble_sort(items, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]


def main():
    items = [1,5,4,2,3,2,1]
    n = len(items)
    bubble_sort(items, n)
    print(items)


main()

