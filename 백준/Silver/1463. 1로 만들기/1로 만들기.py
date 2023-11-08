n = int(input())

dpTable = [0] * (n + 1)

for i in range(2, n + 1):
    cnts = []
    if(i % 3 == 0): cnts.append(dpTable[int(i / 3)] + 1)
    if(i % 2 == 0): cnts.append(dpTable[int(i / 2)] + 1)
    if(i - 1 != 0): cnts.append(dpTable[i - 1] + 1)
    dpTable[i] = min(cnts)

print(dpTable[n])