from copy import deepcopy
from collections import deque

DFSResult = []
BFSResult = []

def DFS(graph, start, visited):
  DFSResult.append(str(start))
  visited[start] = True

  if len(graph[start]) != 0:
    for i in graph[start]:
      if not visited[i]:
        DFS(graph, i, visited)

def BFS(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  
  while len(queue) > 0:
    num = queue.popleft()
    BFSResult.append(str(num))
    for next in graph[num]:
      if not visited[next]: 
        visited[next] = True
        queue.append(next)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
  first, second = map(int, input().split())
  graph[first].append(second)
  graph[second].append(first)

for nodes in graph:
  nodes.sort()

visited = [False] * (N + 1)
DFS(graph, V, deepcopy(visited))
BFS(graph, V, deepcopy(visited))
print(' '.join(DFSResult))
print(' '.join(BFSResult))