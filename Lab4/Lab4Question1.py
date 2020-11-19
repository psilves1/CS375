import random

import sys
sys.setrecursionlimit(1002) #got recursion error without increasing it, 
#python's base recursion limit is 1000, for this we need to make it 1002 for the program to run

def palindromeAlgo(arr, front, back, dictionary):

    if(front < 0 or back >= len(arr) or front > back): #if the front pointer is further in the list than the back pointer
        #NOTE: it's okay for front == back. IF YOU DON'T ALLOW IT YOU WILL MESS THE PROGRAM UP
        return []

    if(front == back):
        return [arr[front]]

    if(front +1 == back): #need to have a nested if statement due to else. Cannot combine with OR statement
        if(arr[front] == arr[back]):
            return [arr[front]] + [arr[back]]
        else:
            return []

        
    if(front, back) not in dictionary: #this is where it becomes dynamic programming
    #if we've calculated it before, we don't need to waste time doing this

        #using retVal variables to make the code more readable
        retVal1 = []
        retVal2 = palindromeAlgo(arr, front+1, back, dictionary) #move back pointer forward one
        retVal3 = palindromeAlgo(arr, front, back-1, dictionary) #move front pointer front one

        if(arr[front] == arr[back]):
            retVal1 = [arr[front]] + palindromeAlgo(arr, front+1, back-1, dictionary) + [arr[back]] #move both forward or both front

        dictionary[(front,back)] = max(retVal1, retVal2, retVal3, key = len)
            

    return dictionary[(front,back)]


arr = [7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15]

x = palindromeAlgo(arr, 0, len(arr) - 1, {})

print(x)
print("Length: " + str(len(x)))

i = 0
arr2 = []

while(i < 1000): 
    arr2.append(random.randint(0,100))

    i+=1

x = palindromeAlgo(arr2, 0, len(arr2) - 1, {})

print("")
print(x)
print("Length: " + str(len(x)))