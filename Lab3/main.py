import random
import time
import copy

from Algorithm1 import randomListSplit
from Algorithm2 import listSplit
from Algorithm3 import sortedSelection

counter = 0

largeList = []
largeList2 = []
largeList3 = []

while (counter < 10**7):
    largeList.append(int(random.uniform(0, 10**7/100)))
    # largeList2.append(int(random.uniform(0, 10**7)))
    # largeList3.append(int(random.uniform(0, 10**7)))

    counter += 1 

timer = time.time()
var = randomListSplit(copy.deepcopy(largeList), 10**7/2)
print("Random Split Algorihtm Time = " + str(time.time() - timer))
print("Var: " + str(var))

timer = time.time()
var = listSplit(copy.deepcopy(largeList), 10**7/2)
print("Deterministic Split Algorihtm Time = " + str(time.time() - timer))
print("Var: " + str(var))


timer = time.time()
var = sortedSelection(largeList, 10**7/2)
print("Random Split Algorihtm Time = " + str(time.time() - timer))
print("Var: " + str(var))



