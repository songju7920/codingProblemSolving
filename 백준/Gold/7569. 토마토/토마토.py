from collections import deque
import sys

MAX = 100
M, N, H = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visit = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
ways = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]

startPoint = []

for i in range(H):
  for j in range(N):
    for k in range(M):
      if graph[i][j][k] == 1:
        startPoint.append([i, j, k])
        visit[i][j][k] = True

def BFS():
  queue = deque(startPoint)

  while queue:
    h, n, m = queue.popleft()

    for way in ways:
      z, y, x = h + way[0], n + way[1], m + way[2]
      if 0 <= z < H and 0 <= y < N and 0 <= x < M and not visit[z][y][x] and graph[z][y][x] != -1:
        graph[z][y][x] = graph[h][n][m] + 1
        queue.append([z, y, x])
        visit[z][y][x] = True

BFS()

maxValue = 0
for i in range(H):
  for j in range(N):
    for k in range(M):
      if graph[i][j][k] > maxValue:
        maxValue = graph[i][j][k]
      if graph[i][j][k] == 0:
        print('-1')
        sys.exit()

print(maxValue - 1)