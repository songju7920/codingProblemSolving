from collections import deque

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

count = {}
for num in nums:
  if num in count:
    count[num] += 1
  else:
    count[num] = 1

for target in targets:
  if target in count:
    print(count[target], end=" ")
  else:
    print(0, end=" ")