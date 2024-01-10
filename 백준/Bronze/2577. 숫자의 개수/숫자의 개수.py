nums = 1
for _ in range(3):
  nums *= int(input())
nums = str(nums)

for i in range(10):
  cnt = 0
  for num in nums:
    if num == str(i): cnt += 1
  print(cnt)