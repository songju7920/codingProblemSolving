T = int(input())


for _ in range(T):
  N = int(input())
  DP = [0] * (N + 5)
  DP[1:6] = [1, 1, 1, 2, 2]

  for i in range(6, N + 1):
    DP[i] = DP[i - 1] + DP[i - 5]
    
  print(DP[N])