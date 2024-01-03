# 1012번 유기농 배추
# 09:37 ~ 10:06 (29분)

from collections import deque

T = int(input())

for _ in range(T):
  result = 0
  M, N, K = map(int ,input().split())
  graph = [[0 for _ in range(M)] for _ in range(N)]
  for _ in range(K):
    x, y = map(int, input().split())
    graph[y][x] = 1

  def BFS(startIdx):
    queue = deque([startIdx])

    while len(queue) > 0:
      x, y = queue.popleft()
      if graph[x][y] == 0: continue
      graph[x][y] = 0
      if x > 0 and graph[x - 1][y] == 1:
        queue.append([x - 1, y])
      if x < N - 1 and graph[x + 1][y] == 1:
        queue.append([x + 1, y])
      if y > 0 and graph[x][y - 1] == 1:
        queue.append([x, y - 1])
      if y < M - 1 and graph[x][y + 1] == 1:
        queue.append([x, y + 1])

  for i in range(N):
    for j in range(M):
      if graph[i][j] == 1:
        result += 1
        BFS([i, j])
  
  print(result)