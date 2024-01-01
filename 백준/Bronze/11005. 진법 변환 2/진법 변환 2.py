alpabets = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''

[N, B] = map(int, input().split())
while N >= B:
  result += alpabets[N % B]
  N //= B
result += alpabets[N]

print(''.join(list(reversed(result))))