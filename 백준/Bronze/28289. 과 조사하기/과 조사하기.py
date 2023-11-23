n = int(input())
result = [0] * 4

for i in range(n):
    [Sgrade, Sclass, Snum] = map(int, input().split())
    if Sgrade == 1: result[3] += 1
    elif Sclass == 1 or Sclass == 2: result[0] += 1
    elif Sclass == 3: result[1] += 1
    elif Sclass == 4: result[2] += 1

for i in range(4): print(result[i])