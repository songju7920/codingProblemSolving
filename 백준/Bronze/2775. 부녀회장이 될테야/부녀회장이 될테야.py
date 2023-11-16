t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    DPTable = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(n + 1): DPTable[0][i] = i
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            DPTable[i][j] = DPTable[i - 1][j] + DPTable[i][j - 1]
    print(DPTable[k][n])