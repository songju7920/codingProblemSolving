from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visted = [[False for _ in range(M)] for _ in range(N)]
movement = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
answer = 0

def BFS(start):
  visted[start[0]][start[1]] = True
  queue = deque([start])
  isToppest = True
  global answer

  while queue:
    currunt = queue.popleft()
    for move in movement:
      nx, ny = currunt[0] + move[0], currunt[1] + move[1]
      if 0 <= nx < N and 0 <= ny < M:
        if graph[currunt[0]][currunt[1]] == graph[nx][ny] and not visted[nx][ny]:
          queue.append([nx, ny])
          visted[nx][ny] = True
        elif graph[currunt[0]][currunt[1]] < graph[nx][ny]:
          isToppest = False
  
  if isToppest:
    answer += 1

for i in range(N):
  for j in range(M):
    if not visted[i][j]:
      BFS([i, j])
print(answer)