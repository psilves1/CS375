from ShortestJob import shortestAlgorithm
from LongestJob import longestAlgorithm
from FCFS import FCFSAlgorithm
from generateJob import generateJobs, Job
from copy import deepcopy

listOfJobs = generateJobs(100)
listOfJobs1 = deepcopy(listOfJobs)
listOfJobs2 = deepcopy(listOfJobs)

waitingTime = []
serviceTime = []
time = 0

time = shortestAlgorithm(listOfJobs, waitingTime, serviceTime)

print("Shortest First:")
totalWaitTime = 0
maxWaitTime = 0
for n in waitingTime:
    totalWaitTime += n

    if(n > maxWaitTime):
        maxWaitTime = n
print("\tTotal  Time: " + "%.3f" % (time))
print("\tAverage Wait Time: " + "%.3f" % (totalWaitTime/100))
print("\tMax Wait Time:     " + "%.3f\n" % (maxWaitTime))



waitingTime = []
serviceTime = []
time = 0

time = longestAlgorithm(listOfJobs1, waitingTime, serviceTime)

print("Longest First:")
totalWaitTime = 0
maxWaitTime = 0
for n in waitingTime:
    totalWaitTime += n

    if(n > maxWaitTime):
        maxWaitTime = n

print("\tTotal  Time: " + "%.3f" % (time))
print("\tAverage Wait Time: " + "%.3f" % (totalWaitTime/100))
print("\tMax Wait Time:     " + "%.3f\n" % (maxWaitTime))

waitingTime = []
serviceTime = []

time = FCFSAlgorithm(listOfJobs2, waitingTime, serviceTime)

print("First Come First Serve:")
totalWaitTime = 0
maxWaitTime = 0
for n in waitingTime:
    totalWaitTime += n

    if(n > maxWaitTime):
        maxWaitTime = n
print("\tTotal  Time: " + "%.3f" % (time))
print("\tAverage Wait Time: " + "%.3f" % (totalWaitTime/100))
print("\tMax Wait Time:     " + "%.3f" % (maxWaitTime))