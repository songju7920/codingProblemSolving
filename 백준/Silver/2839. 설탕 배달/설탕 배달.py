n = int(input())
dpTable = [0] * (n + 3)
dpTable[1] = -1
dpTable[2] = -1
dpTable[3] = 1
dpTable[4] = -1
dpTable[5] = 1

for i in range(6, n + 1):
    cnts = []
    if dpTable[i - 3] != -1: cnts.append(dpTable[i - 3] + 1)
    if dpTable[i - 5] != -1: cnts.append(dpTable[i - 5] + 1)
    dpTable[i] = -1 if len(cnts) == 0 else min(cnts)

print(dpTable[n]) 