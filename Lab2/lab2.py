import random

def randGraph(n, p):

    arr = [[0 for x in range(n)] for y in range(n)] 

    counter1 = 0
    counter2 = 0

    while(counter1 < n):
        counter2 = 0
        while(counter2 < n):
            if(random.random() < p and not (counter1 == counter2)):          
                arr[counter1][counter2] = 1
                arr[counter2][counter1] = 1
            else:
                arr[counter1][counter2] = 0
                arr[counter2][counter1] = 0
            counter2 += 1
        counter1 += 1

    return arr


def findS(graph, marked):
    
    numOfIters = 0

    while(numOfIters < len(graph[0]) *len(graph[0])):
   
        rowVal = 0
        columnVal = 0

        for row in graph:
            for column in row: 
                if column == 1 and not (columnVal == rowVal) and [columnVal, rowVal] not in marked:
                    return [columnVal, rowVal]
                columnVal += 1

            columnVal = 0
            rowVal += 1
        numOfIters += 1

    return [-1,-1]
        

        
    

def bfs(graph, t):

    source = []

    """
    rowVal = 0
    columnVal = 0

    for row in graph:
        for column in row: 
            if column == 1 and not (columnVal == rowVal):
                source = [columnVal, rowVal]
            columnVal += 1

        columnVal = 0
        rowVal += 1
    """

    #source is good 


    queue = []
    marked = []

    source = findS(graph, marked)

    if(source[0] == -1):
        return -1

    queue.append(source)
    marked.append(source)

    while(len(queue) > 0):
        
        v = queue.pop()

        if(v == []):
            break

        index = 0

        for num in graph[v[1]]:
            if([v[1], index] not in marked and num == 1):

                marked.append([v[1], index])
                queue.append([v[1], index])

            index += 1

        index = 0

    return len(marked)#(len(marked)-(len(marked)-1)/2) >= t

def findLargestComp(graph, t):

    numOfEdges = 0

    for c in graph:
        for r in c: 
            if(r == 1): 
                numOfEdges += 1 

    n = 0
    largestCompSize = 0

    while (n < numOfEdges):
        temp = bfs(graph, t)
        if(temp == -1):
            return (largestCompSize-(largestCompSize-1)/2) >= t
        n += temp
        if(temp > largestCompSize):
            largestCompSize = temp

    return (largestCompSize-(largestCompSize-1)/2) >= t
        


def generate(numOfGraphs=500, n=40):
    
    for num in range(2, 32, 2):
        num = num / 10
        p = num / n
        #print(p)

        x = 0
        numOfGoodGraphs = 0

        while(x < numOfGraphs):
            graph = randGraph(n,p)
            #print(graph)
            if(findLargestComp(graph,30)):
                numOfGoodGraphs += 1

            x+= 1

        print("For c = " + str(num) + ", " +  str(round(numOfGoodGraphs/numOfGraphs*100 , 3)) + "% meet the threshold")


generate()
