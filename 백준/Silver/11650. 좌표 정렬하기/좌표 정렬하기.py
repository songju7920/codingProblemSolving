N = int(input())
points = []

for i in range(N):
  points.append(list(map(int, input().split())))

for point in sorted(points):
  print(*point)