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
B=[1,2,3,4,5,6,7,8,9,10]

print(randomListSplit(A,5))
print(randomListSplit(B,5))