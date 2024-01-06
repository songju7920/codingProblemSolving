# 1697번 숨바꼭질

from collections import deque

MAXSIZE = 100000
start, target = map(int, input().split())

graph = [0 for _ in range(MAXSIZE + 1)]
visited = [False for _ in range(MAXSIZE + 1)]

def BFS():
  queue = deque([start])
  visited[start] = True
  while len(queue) > 0:
    current = queue.popleft()
    if current == target: break
    if current - 1 >= 0 and not visited[current - 1]:
      graph[current - 1] = graph[current] + 1
      visited[current - 1] = True
      queue.append(current - 1)
    if current + 1 <= MAXSIZE and not visited[current + 1]:
      graph[current + 1] = graph[current] + 1
      visited[current + 1] = True
      queue.append(current + 1)
    if current * 2 <= MAXSIZE and not visited[current * 2]:
      graph[current * 2] = graph[current] + 1
      visited[current * 2] = True
      queue.append(current * 2)

BFS()
print(graph[target])