n = int(input())

dpTable = [0] * n
dpTable[0] = 1
dpTable[1] = 1

for i in range(2, n):
    dpTable[i] = dpTable[i-1] + dpTable[i-2]

print(dpTable[n - 1], n - 2)