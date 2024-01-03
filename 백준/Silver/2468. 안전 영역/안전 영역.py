# 2468번 안전 영역
# 10:20 ~ 11:07 (47분)

from collections import deque
from copy import deepcopy

N = int(input())
graph = []
maxHeight = 0

for _ in range(N):
  newRow = list(map(int, input().split()))
  maxValue = max(newRow)
  graph.append(newRow)
  if maxHeight < maxValue : maxHeight = maxValue

def chack(graphCopy, height):
  result = 0
  def BFS(startIdx):
    queue = deque([startIdx])
    while len(queue) > 0:
      x, y = queue.popleft()
      if graphCopy[x][y] == 0: continue

      graphCopy[x][y] = 0
      if x > 0 and graphCopy[x - 1][y] > height:
        queue.append([x - 1, y])
      if x < N - 1 and graphCopy[x + 1][y] > height:
        queue.append([x + 1, y])
      if y > 0 and graphCopy[x][y - 1] > height:
        queue.append([x, y - 1])
      if y < N - 1 and graphCopy[x][y + 1] > height:
        queue.append([x, y + 1])

  for i in range(N):
    for j in range(N):
      if graphCopy[i][j] > height and graphCopy[i][j] != 0:
        BFS([i, j])
        result += 1
  
  return result

results = [chack(deepcopy(graph), i) for i in range(maxHeight + 1)]
print(max(results))