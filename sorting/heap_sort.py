import heapq

def heap_sort(items):
    h = []
    for value in items:
        heapq.heappush(h,value)

    result = [heapq.heappop(h) for i in range(len(h))]
    return result



def main():
    items = [1,5,6,4,3,2,9]
    result = heap_sort(items)
    print(result)


main()
