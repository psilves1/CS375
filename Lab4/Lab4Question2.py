import copy

def greedy(arr, weight):

    ratios = sorted(arr, reverse=True, key=lambda n: n[1]/n[0]) #O(n*log(n))

    totalValue = 0

    for n in ratios:    #O(n)
        if(n[0] > weight):
            continue
        weight -= n[0]
        totalValue += n[1]


    print(totalValue)


def dynmaic(arr, weight):
    k = [[0 for x in range(len(arr)+1)] for y in range(weight+1)]

    for j in range(1, len(arr)):
        for w in range(1, weight+1):
            if(arr[j][0] > w):
                k[w][j] = k[w][j-1]
            else:
                k[w][j] = max(k[w][j-1], k [w-arr[j][0]] [j-1] + arr[j][1])
    
    print(k[weight] [len(arr)-1])

    # for i in range(len(k)):
    #     for j in range(len(k[i])):
    #         print(k[i][j], end=' ')
    #     print()





arr=[[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], [100, 94], [100, 96], [102, 97], [103, 97], [104, 99], [
    106, 101], [107, 101], [106, 102], [107, 102], [109, 104], [109, 106], [110, 107], [111, 108], [113, 107], [114, 110]]

print("Greedy: ")
greedy(copy.deepcopy(arr), 100)
greedy(copy.deepcopy(arr), 200)
greedy(copy.deepcopy(arr), 300)

print("\nDynamic: ")
dynmaic(copy.deepcopy(arr), 100)
dynmaic(copy.deepcopy(arr), 200)
dynmaic(copy.deepcopy(arr), 300)
