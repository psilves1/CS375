from generateJob import generateJobs
from generateJob import Job

listOfJobs = generateJobs(100)

def FCFSAlgorithm(listOfJobs, waitingTimeArr, serviceTimeArr):

    orderedJobs = listOfJobs

    prevJob = Job(0,0)
    for job in orderedJobs:
        job.arrivalTime = prevJob.arrivalTime + job.arrivalTime
        prevJob = job

    queue = [orderedJobs.pop(0)]

    time = 0
    while(len(orderedJobs) > 0):

        job = queue.pop(0)

        if (time < job.arrivalTime):
            time = job.arrivalTime

        waitingTimeArr.append(time - job.arrivalTime) 
        serviceTimeArr.append(waitingTimeArr[len(waitingTimeArr) - 1] + job.length) 

        time += job.length

        booleanVar = len(orderedJobs) > 0
        while(booleanVar):
            queue.append(orderedJobs.pop(0))
            booleanVar = len(orderedJobs) > 0 and orderedJobs[0].arrivalTime <= time

    while(len(queue) > 0):
        time += queue.pop(0).length

    return time