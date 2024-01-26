from itertools import combinations

N, K = map(int, input().split())
nums = [i for i in range(N)]

answer = len([i for i in combinations(nums, K)])
print(answer)