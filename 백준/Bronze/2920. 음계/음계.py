nums = list(map(int, input().split()))
result = "started"


for i in range(1, len(nums)):
  if nums[i] >= nums[i - 1] and (result == "started" or result == "ascending"):
    result = "ascending"
  elif nums[i] <= nums[i - 1] and (result == "started" or result == "descending"):
    result = "descending"
  else:
    result = "mixed"
    break

print(result)