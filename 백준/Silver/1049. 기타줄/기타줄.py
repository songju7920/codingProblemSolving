import math

[n, m] = map(int, input().split())
allPrices = [[] for _ in range(m)]
packagePrices = [[] for _ in range(m)]
eachPrices = [[] for _ in range(m)]
totalPrice = 0

for i in range(m): 
    data = list(map(int, input().split()))
    packagePrices[i] = data[0]
    eachPrices[i] = data[1]
    data[0] = data[0] / 6
    allPrices[i] = data

allPrices = sum(allPrices, [])

if n >= 6:
    minPrice = min(allPrices)
    packageCnt = n // 6
    n %= 6
    totalPrice += packageCnt * minPrice * 6
if n > 0:
    minPackagePrice = min(packagePrices)
    minEachPrice = min(eachPrices) * n
    if minEachPrice > minPackagePrice: totalPrice += minPackagePrice
    else: totalPrice += minEachPrice

print(math.ceil(totalPrice))