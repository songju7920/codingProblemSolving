[N, M, P] = list(map(int, input().split()))
isSuccess = True

for i in range(N):
    stages = list(map(int, input().split()))
    if(isSuccess):
        stages.sort()
        itemCnt = 0
        for stage in stages:
            if stage == -1: itemCnt += 1
            elif stage <= P: P += stage
            else:
                while P < stage and itemCnt > 0:
                    itemCnt -= 1
                    P *= 2
                if P >= stage: P += stage
                else:
                    isSuccess = False
                    break
        while itemCnt > 0:
            itemCnt -= 1
            P *= 2

print(int(isSuccess))