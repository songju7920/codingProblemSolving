n = int(input())
DpTable = [0] * (n + 1)
DpTable[0] = [0, 0]
firstScore = int(input())
DpTable[1] = [firstScore, firstScore]

for i in range(2, n + 1):
    results = []
    score = int(input())
    results.append(DpTable[i-2][0] + score)
    results.append(DpTable[i-2][1] + score)
    DpTable[i] = [DpTable[i-1][1] + score, max(results)]

print(max(DpTable[n]))