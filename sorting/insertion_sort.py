def insertion_sort(items):
    for i in range(len(items)):
        j = i 
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j = j - 1

    return items


def main():
    items = [4,5,6,3,2,1]
    items = insertion_sort(items)
    print(items)

main()
