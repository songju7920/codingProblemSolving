def sieveOfEratosthenes(maxNum):
  nums = [i for i in range(2, maxNum + 1)]
  result = []

  while nums:
    nextNum = nums[0]
    result.append(nextNum)
    nums = [num for num in nums if num % nextNum != 0]
  
  return result

# main
N = int(input())
nums = list(map(int, input().split()))

maxVal = max(nums)
primeNums = sieveOfEratosthenes(maxVal)

print(len([num for num in nums if num in primeNums]))