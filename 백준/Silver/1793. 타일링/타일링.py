while True:
  try:
    N = int(input())
    DPTable = [0] * (N + 3)
    DPTable[0] = 1
    DPTable[1] = 1
    for i in range(2, N + 1):
      DPTable[i] = DPTable[i - 1] + DPTable[i - 2] * 2
    print(DPTable[N])
  except:
    break