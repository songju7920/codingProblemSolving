import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
start = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
  startPoint, endPoint, dis = map(int, input().split())
  graph[startPoint].append([endPoint, dis])

def dijkstra():
  dist = [1e9] * (N + 1)
  dist[start] = 0
  queue = []
  heapq.heappush(queue, (0, start))

  while queue:
    cur_dis, cur_point = heapq.heappop(queue)

    if cur_dis > dist[cur_point]:
      continue

    for next, next_dis in graph[cur_point]:
      if dist[next] > cur_dis + next_dis:
        dist[next] = cur_dis + next_dis
        heapq.heappush(queue, (dist[next], next))
  
  return dist

result = dijkstra()
for i in range(1, N + 1):
  print(result[i] if result[i] != 1e9 else 'INF')