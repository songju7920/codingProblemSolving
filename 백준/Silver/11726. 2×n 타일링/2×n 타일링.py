n = int(input())
DpTable = [0] * (n + 2)
DpTable[1] = 1
DpTable[2] = 2

for i in range(3, n + 1):
    DpTable[i] = DpTable[i - 1] + DpTable[i - 2]

print(DpTable[n] % 10007)