def algo(arr1, arr2):

    if(len(arr1) == 0 and len(arr2) == 0):
        return -1

    length1 = len(arr1)
    length2 = len(arr2)

    if(length1 > length2):
        temp = length1
        temp2 = arr1
        length1 = length2
        arr1 = arr2
        length2 = temp
        arr2 = temp2


                
    minVal = 0
    maxVal = length1
    halfLength = (length1 + length2 + 1) / 2

    while maxVal >= minVal:
        x = int((maxVal + minVal) / 2)
        y = int(halfLength - x)
        if x < length1 and arr2[y-1] > arr1[x]:
            minVal = x + 1

        elif x > 0 and arr1[x-1] > arr2[y]:
            maxVal = x - 1

        else:
            if x == 0:
                maxLeft = arr2[y-1]
            elif y == 0: 
                maxLeft = arr1[x-1]
            else: 
                maxLeft = max(arr1[x-1], arr2[y-1])

            if (length1 + length2) % 2 == 1:
                return maxLeft

            if x == length1: 
                minRight = arr2[y]
            elif y == length2:
                 minRight = arr1[x]
            else: 
                minRight = min(arr1[x], arr2[y])

            return (maxLeft + minRight) / 2.0


# arr1 = [2 ,  4 ,  5 ,  6 ,  7]
# arr2 = [20 ,  21 ,  25 ,  30 ,  40]
# print(algo(arr1 , arr2))