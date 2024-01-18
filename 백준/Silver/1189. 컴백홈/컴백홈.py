R, C, K  = map(int, input().split())
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]

graph = [[] for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

for i in range(R):
  graph[i] = list(input())

start = [R - 1, 0]
end = [0, C - 1]

DFSResult = 0
def DFS(currunt, cnt):
  global DFSResult

  # 탈출 조건
  if currunt == end:
    if cnt == K - 1:
      DFSResult += 1
    return

  # 다음 탐색 노드 선택 
  visited[currunt[0]][currunt[1]] = True
  for move in movement:
    nx, ny = currunt[0] + move[0], currunt[1] + move[1]
    if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and graph[nx][ny] != 'T':
      DFS([nx, ny], cnt + 1)

  # 백트래킹
  visited[currunt[0]][currunt[1]] = False
    
DFS(start, 0)
print(DFSResult)