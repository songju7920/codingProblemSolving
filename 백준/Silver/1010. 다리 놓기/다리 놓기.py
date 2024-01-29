T = int(input())

DPTable = [1]

for _ in range(T):
  N, M = map(int, input().split())
  if len(DPTable) < max(N, M) + 1:
    for i in range(len(DPTable), max(N, M) + 1):
      DPTable.append(DPTable[i - 1] * i)
  print(DPTable[M] // (DPTable[N] * DPTable[M - N]))