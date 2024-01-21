from collections import deque

N, M = map(int, input().split())
movement = [[0, 1], [0, -1], [1, 0], [-1, 0]]
graph = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

def BFS(start):
  visited[start[0]][start[1]] = True
  queue = deque([start])

  while queue:
    x, y = queue.popleft()
    for move in movement:
      nx, ny = x + move[0], y + move[1]
      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] != 1:
        queue.append([nx, ny])
        visited[nx][ny] = True
  
for i in range(M):
  if graph[0][i] == 0:
    BFS([0, i])

result = 'NO'
for i in range(M):
  if visited[N - 1][i]:
    result = 'YES'
    break
print(result)