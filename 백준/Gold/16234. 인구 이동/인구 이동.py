import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

N, L, R = map(int, input().split())

graph = [[] for _ in range(N)]
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for i in range(N):
  graph[i] = list(map(int, input().split()))

def BFS(start, visited):
  unity = [start]
  unitySum = graph[start[0]][start[1]]
  queue = deque([start])
  visited[start[0]][start[1]] = True

  while queue:
    cx, cy = queue.popleft()

    for move in movement:
      nx, ny = cx + move[0], cy + move[1]
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <= abs(graph[cx][cy] - graph[nx][ny]) <= R:
        unitySum += graph[nx][ny]
        visited[nx][ny] = True
        unity.append([nx, ny])
        queue.append([nx, ny])
  
  unityVal = unitySum // len(unity)
  for x, y in unity:
    graph[x][y] = unityVal

answer = 0
while True:
  beforeGraph = deepcopy(graph)
  visited = [[False] * N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      if not visited[i][j]:
        BFS([i, j], visited)

  if beforeGraph == graph:
    break

  answer += 1

print(answer)