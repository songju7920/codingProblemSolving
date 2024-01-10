import sys
input = sys.stdin.readline
N = int(input())

nums = [int(input()) for _ in range(N)]
for num in sorted(nums):
  print(num)