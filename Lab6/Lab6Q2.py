import sys

def func2(arr, bottom, mid, top) : 
      
    sm = 0
    leftSum = -sys.maxsize - 1 #smallest possible number
      
    for i in range(mid, bottom-1, -1) : 
        sm = sm + arr[i] 
          
        if (sm > leftSum) : 
            leftSum = sm 
      
    sm = 0
    rightSum = -sys.maxsize - 1 #smallest possible num
    for i in range(mid + 1, top + 1) : 
        sm = sm + arr[i] 
          
        if (sm > rightSum) : 
            rightSum = sm 

    return max(leftSum + rightSum, leftSum, rightSum) 
  
  
def func1(arr, bottom, top) : 
      
    if (bottom == top) : 
        return arr[bottom] 
  
    mid = int((bottom + top) / 2) #mid point
  
    retVal1 = func1(arr,bottom,top)
    retVal2 = func1(arr, mid + 1, top)
    retVal3 = func2(arr, bottom, mid, top)

    maxRetVal = max(retVal1, retVal2, retVal3)

    return maxRetVal 

arr = [6 ,-2 , -2, 20 , -3, -2,  4]

print(func1(arr, 0, len(arr) - 1))