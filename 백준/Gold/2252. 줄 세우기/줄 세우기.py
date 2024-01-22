from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
inDegree = [0 for _ in range(N + 1)]
visted = [False for _ in range(N + 1)]
inDegree[0] = -1

for _ in range(M):
  first, second = map(int, input().split())
  graph[first].append(second)
  inDegree[second] += 1


def BFS(start):
  result = []
  queue = deque(start)
  for i in start:
    visted[i] = True

  while queue:
    currunt = queue.popleft()
    result.append(currunt)

    for next in graph[currunt]:
      if inDegree[next] > 0:
        inDegree[next] -= 1
      if not visted[next] and inDegree[next] == 0:
        queue.append(next)
        visted[next] = True
  
  return result

startNums = []
for i in range(1, N + 1):
  if inDegree[i] == 0:
    startNums.append(i)
print(*BFS(startNums))