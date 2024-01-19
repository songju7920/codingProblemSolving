import math

T = int(input())

for _ in range(T):
  dots = list(map(int, input().split()))
  start, end = dots[:2], dots[2:]
  answer = 0

  N = int(input())
  for i in range(N):
    x, y, r = map(int, input().split())
    disStart = math.sqrt(abs(start[0] - x) ** 2 + abs(start[1] - y) ** 2)
    disEnd = math.sqrt(abs(end[0] - x) ** 2 + abs(end[1] - y) ** 2)

    if disStart <= r and disEnd <= r:
      continue
    elif disStart <= r:
      answer += 1
    elif disEnd <= r:
      answer += 1

  print(answer)