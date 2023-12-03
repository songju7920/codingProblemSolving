import sys

while True:
  num = sys.stdin.readline()
  if num == "": break

  nums = list(map(int, num.rstrip().split()))

  print(nums[1] // (nums[0] + 1))