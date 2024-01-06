from collections import deque

top, current, target, up, down = map(int, input().split())

graph = [0 for _ in range(top + 1)]
visited = [False for _ in range(top + 1)]
graph[target] = -1
graph[current] = 0

def BFS():
  queue = deque([current])
  visited[current] = True
  while len(queue) > 0:
    floor = queue.popleft()
    if target == floor: break
    if floor + up <= top and not visited[floor + up]:
      queue.append(floor + up)
      visited[floor + up] = True
      graph[floor + up] = graph[floor] + 1
    if floor - down > 0 and not visited[floor - down]:
      queue.append(floor - down)
      visited[floor - down] = True
      graph[floor - down] = graph[floor] + 1

BFS()
print(graph[target] if graph[target] != -1 else "use the stairs")