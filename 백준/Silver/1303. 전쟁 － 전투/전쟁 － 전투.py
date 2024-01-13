N, M = map(int, input().split())
graph = [input() for _ in range(M)]

movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[False for _ in range(N)] for _ in range(M)]

result = [0, 0]
DFSResult = 0

def DFS(start ,target):
  global DFSResult
  x, y = start
  DFSResult += 1
  visited[x][y] = True
  for move in movement:
    nx, ny = x + move[0], y + move[1]
    if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == target:
      DFS([nx, ny], target)

for i in range(M):
  for j in range(N):
    if not visited[i][j]:
      if graph[i][j] == 'W':
        DFS([i, j], 'W')
        result[0] += DFSResult ** 2
      elif graph[i][j] == 'B':
        DFS([i, j], 'B')
        result[1] += DFSResult ** 2
      DFSResult = 0

print(result[0], result[1])