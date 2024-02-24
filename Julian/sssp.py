# https://dmoj.ca/problem/sssp
nm = input().split()
n = int(nm[0])
m = int(nm[1])

graph = {}
visited = set()
values = [float("inf")]*n

for i in range(0, m):
    edge = list(map(int, input().split())) # u, v, w

    firstNode = edge[0]-1
    secondNode = edge[1]-1
    weight = edge[2]

    if not firstNode in graph:
        graph[firstNode] = []

    graph[firstNode].append((secondNode, weight))

    if not secondNode in graph:
        graph[secondNode] = []

    graph[secondNode].append((firstNode, weight))

current = 0
runningTotal = 0
while len(visited) != n:
    visited.add(current)

    if runningTotal < values[current]:
        values[current] = runningTotal

    smallest = float("inf")
    smallestIndex = -1
    for edge in graph[current]:

        if edge[1] < smallest and not edge[0] in visited:
            smallestIndex = edge[0]
            smallest = edge[1]

        if runningTotal + edge[1] < values[edge[0]]:
            values[edge[0]] = runningTotal + edge[1]
    
    if smallestIndex == -1:
        break

    current = smallestIndex
    runningTotal += smallest

for i in range(len(values)):
    if values[i] == float("inf"):
        values[i] = -1
    
    print(values[i])