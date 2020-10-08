import random
from functools import reduce
class Job:

    def __init__(self, length, arrivalTime):
        self.length = length
        self.arrivalTime = arrivalTime

"""
n is the number of jobs you want to generate

returns array of jobs
"""
def generateJobs(n):
    arr = []

    #arr.append(Job(random.randint(50,100) / 100, 0))#first job needs to arrive with an arrival time of 0
    
    i = 0

    while(i < n):
        arr.append(Job(random.randint(50,100) / 100, random.randint(0,100) / 100))

        i += 1

    return arr
    
