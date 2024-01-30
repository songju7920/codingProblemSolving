from collections import deque

N = int(input())
graph = [input() for _ in range(N)]
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]

visited1 = [[False for _ in range(N)] for _ in range(N)]
visited2 = [[False for _ in range(N)] for _ in range(N)]

def BFS1(start, target):
  queue = deque([start])
  visited1[start[0]][start[1]] = True

  while queue:
    point = queue.popleft()
    for move in movement:
      nx, ny = move[0] + point[0], move[1] + point[1]
      if 0 <= nx < N and 0 <= ny < N and not visited1[nx][ny] and graph[nx][ny] == target:
        visited1[nx][ny] = True
        queue.append([nx, ny])
  
def BFS2(start, target):
  queue = deque([start])
  visited2[start[0]][start[1]] = True

  while queue:
    point = queue.popleft()
    for move in movement:
      nx, ny = move[0] + point[0], move[1] + point[1]
      if 0 <= nx < N and 0 <= ny < N and not visited2[nx][ny]:
        if target == 'R' and graph[nx][ny] == 'G' or target =='G' and graph[nx][ny] == 'R' or target == graph[nx][ny]:
          visited2[nx][ny] = True
          queue.append([nx, ny])

result = [0, 0]
for i in range(N):
  for j in range(N):
    if not visited1[i][j]:
      result[0] += 1
      BFS1([i, j], graph[i][j])
    if not visited2[i][j]:
      result[1] += 1
      BFS2([i, j], graph[i][j])
      

print(*result)