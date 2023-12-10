sits = [0] * 101
n = int(input())
data = map(int, input().split())
result = 0

for i in data:
  if sits[i] == 0: sits[i] = 1
  else: result += 1

print(result)