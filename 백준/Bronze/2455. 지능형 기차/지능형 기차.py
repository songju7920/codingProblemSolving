cnt = 0
maxCnt = 0

for i in range(4):
    [left, ride] = map(int, input().split())
    cnt = cnt + ride - left
    if maxCnt < cnt: maxCnt = cnt

print(maxCnt)