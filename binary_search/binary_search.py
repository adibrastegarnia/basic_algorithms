def binary_search(items, l, r,target):
    while l<=r:
        mid = (l+r)/2

        if items[mid] == target:
            return mid

        if items[mid] < target:
            l = mid +1
        elif items[mid] > target:
            r = mid - 1
    return -1


def main():
    items = [1,2,3,4,5,6,7,8,9]
    l = 0
    r = (len(items)) - 1
    target = 10
    result = binary_search(items, l, r,target)
    if result == -1:
        print("Element is not present in the list")
    else:
        print("element is present at indext:",result)


main()

            

