t = int(input())

for i in range(0, t):
    n = int(input())

    dpTable = [0] * (n + 3)
    dpTable[1] = 1
    dpTable[2] = 2
    dpTable[3] = 4

    for j in range (4, n + 1):
        dpTable[j] += dpTable[j-1] + dpTable[j-2] + dpTable[j-3]

    print(dpTable[n])