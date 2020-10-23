def sortedSelection(arr, k):
    quick_sort(arr, 0, len(arr) -1)
    #sorted(arr)
    return arr[int(k-1)]


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1


        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

A=[5, 14, 9, 9, 11, 6, 13, 6, 16, 9] 


#print(sortedSelection(A,5))

C = [4, 16, 19, 9, 17, 2, 11, 16, 8, 16, 9, 14, 9, 11, 8, 13, 10, 9, 14, 17]

# print(sortedSelection(C,10))
# print(sortedSelection(C,3))