# 1534번 안녕

N = int(input())
stamina = [0] + list(map(int, input().split()))
happiness = [0] + list(map(int, input().split()))

DPTable = [[0 for _ in range(100)] for  _ in range(N + 1)]

for i in range(1, N + 1):
  for j in range(1, 100):
    if j < stamina[i]: DPTable[i][j] = DPTable[i - 1][j]
    else: DPTable[i][j] = max(DPTable[i - 1][j], DPTable[i - 1][j - stamina[i]] + happiness[i])

print(DPTable[N][99])