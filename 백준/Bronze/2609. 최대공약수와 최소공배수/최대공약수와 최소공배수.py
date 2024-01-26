def gcd(a, b):
  if a % b == 0: return b
  return gcd(b, a % b)


nums = list(map(int, input().split()))
bigger, smaller = max(nums), min(nums)

gcdValue = gcd(bigger, smaller)
print(gcdValue)
print(bigger * smaller // gcdValue)