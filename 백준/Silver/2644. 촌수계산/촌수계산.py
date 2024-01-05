# 2644번 촌수 계산

from collections import deque

N = int(input())
start, target = list(map(int, input().split()))
M = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
results = [0 for _ in range(N + 1)]

for _ in range(M):
  first, second = map(int, input().split())
  graph[first].append(second)
  graph[second].append(first)

def BFS():
  queue = deque([start])
  while len(queue) > 0:
    current = queue.popleft()
    visited[current] = True
    if current == target: break
    for next_node in graph[current]:
      if not visited[next_node]:
        queue.append(next_node)
        results[next_node] = results[current] + 1

BFS()
print(results[target] if results[target] != 0 else -1)