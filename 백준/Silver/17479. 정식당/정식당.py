import sys

# 메뉴 입력받기
[a, b, c] = map(int, sys.stdin.readline().split())
hashMapA = dict()
hashMapB = dict()

for i in range(a):
    [menu, price] = sys.stdin.readline().split()
    hashMapA[menu] = int(price)

for i in range(b):
    [menu, price] = sys.stdin.readline().split()
    hashMapB[menu] = int(price)

for i in range(c):
    menu = sys.stdin.readline()

# 주문받기
n = int(sys.stdin.readline())
cnts = [0, 0, 0]

for i in range(n):
    menu = sys.stdin.readline().rstrip()
    if menu in hashMapA.keys(): cnts[0] += hashMapA[menu]
    elif menu in hashMapB.keys(): cnts[1] += hashMapB[menu]
    else: cnts[2] += 1

if cnts[0] < 20000 and cnts[1] > 0: print('No')
elif cnts[0] + cnts[1] < 50000 and cnts[2] > 0: print('No')
elif cnts[2] > 1: print('No')
else: print('Okay')