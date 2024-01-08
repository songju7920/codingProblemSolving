stuffCnt, limit = map(int, input().split())

stuffs = [[0, 0]] + [list(map(int, input().split())) for _ in range(stuffCnt)]

DPTable = [[0 for _ in range(limit + 1)] for _ in range(stuffCnt + 1)]

for i in range(1, stuffCnt + 1):
  for j in range(1, limit + 1):
    sw, sv = stuffs[i]
    if j < sw: DPTable[i][j] = DPTable[i - 1][j]
    else: DPTable[i][j] = max(DPTable[i - 1][j], DPTable[i - 1][j - sw] + sv)

print(DPTable[stuffCnt][limit])