def chackDrow(start, graph):
  result = [0, 0]
  for i in range(start[0], start[0] + 8):
    for j in range(start[1], start[1] + 8):
      if (i + j) % 2 == 0:
        if graph[i][j] == 'W':
          result[0] += 1
        elif graph[i][j] == 'B':
          result[1] += 1
      else:
        if graph[i][j] == 'B':
          result[0] += 1
        elif graph[i][j] == 'W':
          result[1] += 1

  return min(result)

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
answers = []

for i in range(N - 7):
  for j in range(M - 7):
    answers.append(chackDrow([i, j], graph))

print(min(answers))