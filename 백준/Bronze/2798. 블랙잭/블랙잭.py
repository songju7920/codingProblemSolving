from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = sum(nums[:3])

for i in combinations(nums, 3):
  if abs(sum(i) - M) < abs(answer - M) and sum(i) <= M:
    answer = sum(i)

print(answer)