[N, M] = map(int, input().split())

prices = [int(input()) for _ in range(M)]
prices.sort()
if N < M: prices = prices[-N:]

maxNum = 0
result = 0
length = len(prices)
for price in prices:
  if price * length > result: 
    maxNum = price
    result = price * length
  length -= 1

print(maxNum, result)