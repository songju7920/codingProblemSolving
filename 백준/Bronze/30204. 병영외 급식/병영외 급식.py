[n, x] = map(int, input().split())
nums = map(int, input().split())
print(int(sum(nums) % x == 0))