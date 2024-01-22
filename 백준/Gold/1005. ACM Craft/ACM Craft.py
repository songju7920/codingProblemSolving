from collections import deque

T = int(input())

for _ in range(T):
  N, M = map(int, input().split())
  times = [-1] + list(map(int, input().split()))
  DPTable = [0] * (N + 1)

  graph = [[] for _ in range(N + 1)]
  visited = [False] * (N + 1)
  inDegree = [0] * (N + 1)
  inDegree[0] = -1

  for i in range(M):
    first, second = map(int, input().split())
    graph[first].append(second)
    graph[second].append(first)
    inDegree[second] += 1
  tartget = int(input())
  
  def BFS(start):
    queue = deque(start)
    for i in start:
      visited[i] = True

    while queue:
      currunt = queue.popleft()

      results = [0]
      for next in graph[currunt]:
        if inDegree[next] != 0:
          inDegree[next] -= 1
        if not visited[next] and inDegree[next] == 0:
          queue.append(next)
          visited[next] = True
        elif visited[next]:
          results.append(DPTable[next])
      
      DPTable[currunt] = max(results) + times[currunt]
      if currunt == tartget: break

  startPoints = []
  for i in range(1, N + 1):
    if inDegree[i] == 0:
      startPoints.append(i)
  BFS(startPoints)
  print(DPTable[tartget])