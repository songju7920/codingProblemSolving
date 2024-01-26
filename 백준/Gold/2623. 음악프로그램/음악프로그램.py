from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
inDegree = [0] * (N + 1)
inDegree[0] = -1

for _ in range(M):
  K, *singers = list(map(int, input().split()))
  for i in range(K - 1):
    graph[singers[i]].append(singers[i + 1])
    inDegree[singers[i + 1]] += 1

def BFS (startPoint):
  result = []
  queue = deque(startPoint)
  visited = [False for _ in range(N + 1)]

  for point in startPoint:
    visited[point] = True

  while queue:
    point = queue.popleft()
    result.append(point)

    for nextPoint in graph[point]:
      inDegree[nextPoint] -= 1
      if not visited[nextPoint] and inDegree[nextPoint] == 0:
        visited[nextPoint] = True
        queue.append(nextPoint)
  
  return result

startPoint = [i for i in range(1, N + 1) if inDegree[i] == 0]
result = BFS(startPoint)

if len(result) != N:
  print(0)
else:
  for point in result:
    print(point)