from collections import deque

N = int(input())
graph = [[] for _ in range(N)]
results = []
houseCnt = 0

for i in range(N):
  graph[i] = list(map(int ,input()))

def BFS(startIdx):
  queue = deque([startIdx])
  cnt = 0
  while queue:
    x, y = queue.popleft()
    if graph[x][y] == 0: continue
    cnt += 1
    graph[x][y] = 0
    if x > 0 and graph[x - 1][y] == 1:
      queue.append([x - 1, y])
    if x < N - 1 and graph[x + 1][y] == 1:
      queue.append([x + 1, y])
    if y > 0 and graph[x][y - 1] == 1:
      queue.append([x, y - 1])
    if y < N - 1 and graph[x][y + 1] == 1:
      queue.append([x, y + 1])
      
  return cnt

for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      results.append(BFS([i, j]))
      houseCnt += 1

results.sort()
print(houseCnt)
for result in results:
  print(result)
