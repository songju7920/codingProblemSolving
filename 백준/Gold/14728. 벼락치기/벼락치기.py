N, time = map(int, input().split())
tests = []

DPTable = [[0 for _ in range(time + 1)] for _ in range(N + 1)]

for _ in range(N):
  tests.append(list(map(int, input().split())))
tests = [[0, 0]] + tests

for i in range(1, N + 1):
  for j in range(1, time + 1):
    if j < tests[i][0]: DPTable[i][j] = DPTable[i - 1][j]
    else: DPTable[i][j] = max(DPTable[i - 1][j], DPTable[i - 1][j - tests[i][0]] + tests[i][1])

print(DPTable[N][time])