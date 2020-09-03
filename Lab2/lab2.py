import random

def randGraph(n, p):

    arr = [[0 for x in range(n)] for y in range(n)] 

    counter1 = 0
    counter2 = 0

    while(counter1 < n):
        counter2 = 0
        while(counter2 < n):
            if(random.random() < p):
                arr[counter1][counter2] = 1
                arr[counter2][counter1] = 1
            else:
                arr[counter1][counter2] = 0
                arr[counter2][counter1] = 0
            counter2 += 1
        counter1 += 1

    return arr

def vertCount(graph, t):

    num = 0

    for row in graph:
        for x in row:
            num += x
        if(num >= t):
            return 1
        num = 0

    return 0

graph = randGraph(5, .5)

for x in graph:
    print (x)


print("\n")
print(vertCount(graph, 4))