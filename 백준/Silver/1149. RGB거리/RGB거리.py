N = int(input())

DPTable = [[0 for _ in range(3)] for _ in range(N + 1)]
DPTable[1] = list(map(int, input().split()))

for i in range(2, N + 1):
  r, g, b = list(map(int, input().split()))
  DPTable[i][0] = min(DPTable[i - 1][1] + r, DPTable[i - 1][2] + r)
  DPTable[i][1] = min(DPTable[i - 1][0] + g, DPTable[i - 1][2] + g)
  DPTable[i][2] = min(DPTable[i - 1][0] + b, DPTable[i - 1][1] + b)

print(min(DPTable[N]))