t = int(input())

for _ in range(t):
    n = int(input())
    DPTable = [[0, 0]] * (n + 2)
    DPTable[0] = [1, 0]
    DPTable[1] = [0, 1]

    for i in range(2, n + 1):
        DPTable[i] = [DPTable[i - 1][0] + DPTable[i - 2][0], DPTable[i - 1][1] + DPTable[i - 2][1]]

    print(DPTable[n][0], DPTable[n][1])