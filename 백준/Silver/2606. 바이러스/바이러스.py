from collections import deque

def BFS(start, graph, N):
  queue = deque([start])
  isHacked = [False for _ in range(N + 1)]

  while len(queue) > 0:
    com = queue.popleft()
    isHacked[com] = True
    for nextCom in graph[com]:
      if not isHacked[nextCom]:
        queue.append(nextCom)
  
  return isHacked

comCnt = int(input())
relationCnt = int(input())

graph = [[] for _ in range(comCnt + 1)]

for _ in range(relationCnt):
  com1, com2 = map(int, input().split())
  graph[com1].append(com2)
  graph[com2].append(com1)

print(BFS(1, graph, comCnt).count(True) - 1)