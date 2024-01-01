dots = 2
N = int(input())

for _ in range(N):
  dots += dots - 1

print(dots * dots)