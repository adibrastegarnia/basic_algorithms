def selection_sort(items):
    for i in range(len(items)):
        least = i
        for k in range(i+1, len(items)):
            if items[k] < items[least]:
                least = k
        swap(items, least, i)
    return items


def swap(A, x, y):
    A[x], A[y] = A[y], A[x]

def main():
    items = [4,5,3,2,1,7,8]
    items = selection_sort(items)
    print(items)

main()
