N = int(input())
DPTable = [[0, 0, 0] for _ in range(N + 2)]
wines = [int(input()) for _ in range(N)]
wines.append(0)

DPTable[1] = [wines[0], 0, 0]
DPTable[2] = [wines[1], wines[0] + wines[1], wines[0]]

for i in range(3, N + 1):
  DPTable[i][0] = DPTable[i - 1][2] + wines[i - 1]
  DPTable[i][1] = DPTable[i - 1][0] + wines[i - 1]
  DPTable[i][2] = max(DPTable[i - 1])

print(max(DPTable[N]))
