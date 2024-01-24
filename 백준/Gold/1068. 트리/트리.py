from collections import deque

N = int(input())
data = list(map(int, input().split()))
target = int(input())

graph = [[] for _ in range(N)]
startNode = 0
for i in range(N):
  if data[i] != -1:
    graph[data[i]].append(i)
  else:
    startNode = i

def BFS(startNode):
  result = 0
  queue = deque([startNode])
  visited = [False] * N
  visited[startNode] = True
  if startNode == target:
    return 0

  while queue:
    curruntNode = queue.popleft()
    
    if len(graph[curruntNode]) == 0:
      result += 1
      continue
    
    for nextNode in graph[curruntNode]:
      if not visited[nextNode] and nextNode != target:
        queue.append(nextNode)
        visited[nextNode] = True
      elif nextNode == target and len(graph[curruntNode]) == 1:
        result += 1

  return result

print(BFS(startNode))