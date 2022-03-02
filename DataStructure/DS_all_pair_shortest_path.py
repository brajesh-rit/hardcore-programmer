"""
Floyd-Warshall All Pairs Shortest Path Problem
Dynamic Programming
"""
def allPairShortestPath(arr):
    n = len(arr[0])
    inter =[[-1 for _ in range(n)] for _ in range(n)]
    for k in range(1,n):
        for row in range(1,n):
            for col in range(1,n):
                inter[row][col] = min(arr[row][col], (arr[row][k] + arr[k][col]))
        arr = inter

arr = [[0,3,float('inf'),7],[8,0,2,float('inf')],[5,float('inf'),0,1],[2,float('inf'),float('inf'),0]]
allPairShortestPath(arr)
print(arr)