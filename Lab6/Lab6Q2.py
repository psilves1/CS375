import sys

def func1(arr, bottom, top) : 
      
    if (top == bottom) : #base case of recursion
        return arr[bottom] 
  
    mid = int((bottom + top) / 2) #mid point
  
    retVal1 = func1(arr,bottom,mid) #recursion on list half the size
    retVal2 = func1(arr, mid + 1, top) #recursion on list half the size
    retVal3 = func2(arr, bottom, mid, top) 

    maxRetVal = max(retVal1, retVal2, retVal3)

    return maxRetVal 

def func2(arr, bottom, mid, top) : 
      
    sum = 0
    leftSum = -sys.maxsize - 1 #smallest possible number
      
    #needs to be -1 since you're moving left of the point
    for i in range(mid, bottom-1, -1) : 
        sum = sum + arr[i] 
          
        if (sum > leftSum) : 
            leftSum = sum 
      
    sum = 0
    rightSum = -sys.maxsize - 1 #smallest possible num
    for i in range(mid + 1, top + 1) : 
        sum = sum + arr[i] 
          
        if (sum > rightSum) : 
            rightSum = sum 

    retVal1 = leftSum
    retVal2 = rightSum
    retVal3 = leftSum + rightSum

    maxRetVal = max(retVal1, retVal2, retVal3)

    return maxRetVal 
  
  


# arr = [6 ,-2 , -2, 20 , -3, -2,  4]

# print(func1(arr, 0, len(arr) - 1))