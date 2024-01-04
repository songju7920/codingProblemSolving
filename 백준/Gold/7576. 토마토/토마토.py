# 7576번 토마토

from collections import deque
from copy import deepcopy
import sys

M, N = map(int, input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int, input().split())))

def BFS(start):
  visited = [[False for _ in range(M)] for _ in range(N)]
  queue = deque(start)

  while len(queue) > 0: 
    x, y = queue.popleft()

    if x > 0 and graph[x - 1][y] == 0 and not visited[x - 1][y]:
      queue.append([x - 1, y])
      graph[x - 1][y] = graph[x][y] + 1
      visited[x - 1][y] = True
    if x < N - 1 and graph[x + 1][y] == 0 and not visited[x + 1][y]:
      queue.append([x + 1, y])
      graph[x + 1][y] = graph[x][y] + 1
      visited[x + 1][y] = True
    if y > 0 and graph[x][y - 1] == 0 and not visited[x][y - 1]:
      queue.append([x, y - 1])
      graph[x][y - 1] = graph[x][y] + 1
      visited[x][y - 1] = True
    if y < M - 1 and graph[x][y + 1] == 0 and not visited[x][y + 1]:
      queue.append([x, y + 1])
      graph[x][y + 1] = graph[x][y] + 1
      visited[x][y + 1] = True

starts = []

for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      starts.append([i, j])

BFS(starts)

maxResult = 0
for i in range(N):
  for j in range(M):
    if maxResult < graph[i][j]:
      maxResult = graph[i][j]
    elif graph[i][j] == 0:
      print('-1')
      sys.exit()

print(maxResult - 1)