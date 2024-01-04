# 2178번 미로 탐색

from collections import deque

def BFS(graph, start, size):
  result = 0
  queue = deque([start])
  
  while len(queue) > 0:
    x, y = queue.popleft()
    if graph[x][y] == 0: continue

    if x == size[0] - 1 and y == size[1] - 1: 
      result = graph[x][y]
      break

    if x > 0 and graph[x - 1][y] == 1:
      queue.append([x - 1, y])
      graph[x - 1][y] += graph[x][y]
    if x < size[0] - 1 and graph[x + 1][y] == 1:
      queue.append([x + 1, y])
      graph[x + 1][y] += graph[x][y]
    if y > 0 and graph[x][y - 1] == 1:
      queue.append([x, y - 1])
      graph[x][y- 1] += graph[x][y]
    if y < size[1] - 1 and graph[x][y + 1] == 1:
      queue.append([x, y + 1])
      graph[x][y + 1] += graph[x][y]

    graph[x][y] = 0

  return result

N, M = map(int, input().split())
graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

print(BFS(graph, [0, 0], [N, M]))