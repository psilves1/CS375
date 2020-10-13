def determineisticSelection(arr):

    if(len(arr) <= 10):
        arr.sort()
        return(arr[int(len(arr)/2)])

    bigList = []
    smallList = []

    while(len(arr) > 0): 

        index = 0

        #fills up small list 
        while(len(smallList) != 5 and len(arr) > 0):
            smallList.append(arr.pop(index))
            index += 1

        smallList.sort()

        if(len(smallList) % 2 == 0):
            for n in smallList:
                bigList.append(n)
        else:
            bigList.append(smallList[int(len(smallList)/2)])

        smallList = []


    return determineisticSelection(bigList)


def listSplit(arr, k):
    
    v = determineisticSelection(arr)

    lessThanV, equalToV, greaterThanV = [], [], []

    for num in arr:
        if (num < v): 
                lessThanV.append(num)
        elif (num == v):
            equalToV.append(num)
        else:
            greaterThanV.append(num)

    if(k <= len(lessThanV)):
        return listSplit(lessThanV, k)
    k -= len(lessThanV)
    if(k <= len(equalToV)):
        return v
    k -= len(equalToV)
    return listSplit(greaterThanV, k)

A=[5, 14, 9, 9, 11, 6, 13, 6, 16, 9] 
B=[1,2,3,4,5,6,7,8,9,10]

print(listSplit(A,5))
print(listSplit(B,5))