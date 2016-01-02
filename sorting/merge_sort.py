def merge_sort(items):
    
  if len(items) > 1:  
    mid = (len(items)/2)
    left = items[0:mid]
    right = items[mid:]

    merge_sort(left)
    merge_sort(right)


    l, r = 0, 0

    for i in range(len(items)):

        lval = left[l] if l < len(left) else None
        rval = right[r] if r < len(right) else None

        if (lval and rval and lval < rval) or rval is None:
            items[i] = lval
            l = l + 1
        elif (lval and rval and lval >= rval) or lval is None:
            items[i] = rval
            r = r + 1

        else:
            raise Exception("could not merge")

  return items


def main():
    items = [5,4,3,2,6,7]
    items = merge_sort(items)
    print(items)
main()

