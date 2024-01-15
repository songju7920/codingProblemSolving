import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
  com1, com2 = map(int, input().split())
  graph[com2].append(com1)

def DFS(start):
  result = 1
  visited = [False for _ in range(N + 1)]
  visited[i] = True
  queue = deque([i])

  while queue:
    currunt = queue.popleft()
    for next in graph[currunt]:
      if not visited[next]:
        visited[next] = True
        queue.append(next)
        result += 1

  return result

answer = []
maxAnswer = 1
for i in range(1, N + 1):
  result = DFS(i)

  if maxAnswer < result:
    maxAnswer = result
    answer = [i]
  elif maxAnswer == result:
    answer.append(i)

print(*answer)