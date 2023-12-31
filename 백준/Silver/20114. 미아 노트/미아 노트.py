[N, H, W] = map(int, input().split())

isRecovered = [False for _ in range(N)]
recoveredStr = ['?'] * N

for i in range(H):
  damagedStr = input()
  temp = 0
  for idx in range(0, N * W, W):
    if not isRecovered[temp]:
      for char in damagedStr[idx:idx + W]:
        if char != '?':
          isRecovered[temp] = True
          recoveredStr[temp] = char
    temp += 1

print(''.join(recoveredStr))