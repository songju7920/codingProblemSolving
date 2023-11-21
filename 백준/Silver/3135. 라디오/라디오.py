import sys

[start, end] = map(int, input().split())
n = int(input())
min = start

for _ in range(n):
    Hz = int(sys.stdin.readline().rstrip())
    if abs(end - min) > abs(end - Hz): min = Hz

result = abs(end - min)
if start != min: result += 1
print(result)