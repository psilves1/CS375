def sortedSelection(arr, k):
    quick_sort(arr, 0, len(arr) -1)
    return arr[k-1]


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

        while pivot <= array[high] and high >= low:
            high = high - 1

        while pivot >= array[low] and high >= low:
            low = low + 1

        if high >= low:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


A=[5, 14, 9, 9, 11, 6, 13, 6, 16, 9] 
B=[1,2,3,4,5,6,7,8,9,10]

print(sortedSelection(A,5))
print(sortedSelection(B,5))