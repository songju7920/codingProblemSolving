N = int(input())
data = list(reversed(list(map(int, input().split()))))
answer = []

for i in range(N):
  idx = data[i]
  answer = answer[:idx] + [N - i] + answer[idx:]

print(*answer)