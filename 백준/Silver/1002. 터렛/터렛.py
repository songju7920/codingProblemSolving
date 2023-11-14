import math

t = int(input())

for _ in range(t):
    [x1, y1, r1, x2, y2, r2] = list(map(int, input().split()))
    dis1 = abs(x1 - x2)
    dis2 = abs(y1 - y2)
    dis = math.sqrt(pow(dis1, 2) + pow(dis2, 2))
    rRange1 = r1 + r2
    rRange2 = abs(r1 - r2)
    
    if dis == 0 and r1 == r2: print(-1) # 일치함
    elif rRange2 < dis < rRange1: print (2) # 두점에서 만남
    elif rRange1 == dis: print(1) # 외접함
    elif rRange2 == dis: print(1) # 내접합
    else: print(0) # 그외