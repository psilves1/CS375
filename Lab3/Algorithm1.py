import random

"""
Input: an unordered array A[1,...,n] and a number k such that 1<=k<=n
Output: the k-th smallest element in A
"""

def randomListSplit(arr, k):

    v = random.randint(0, len(arr)-1)

    v = arr[v]

    lessThanV, equalToV, greaterThanV = [], [], []

    for num in arr:
        if (num < v): 
                lessThanV.append(num)
        elif (num == v):
            equalToV.append(num)
        else:
            greaterThanV.append(num)

    if(k <= len(lessThanV)):
        return randomListSplit(lessThanV, k)
    k -= len(lessThanV)
    if(k <= len(equalToV)):
        return v
    k -= len(equalToV)
    return randomListSplit(greaterThanV, k)


A=[5, 14, 9, 9, 11, 6, 13, 6, 16, 9] 

print(randomListSplit(A,5))

C = [4, 16, 19, 9, 17, 2, 11, 16, 8, 16, 9, 14, 9, 11, 8, 13, 10, 9, 14, 17]

print(randomListSplit(C,10))