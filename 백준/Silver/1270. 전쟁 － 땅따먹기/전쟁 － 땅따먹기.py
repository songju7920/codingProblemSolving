T = int(input())

for _ in range(T):
  data = list(map(int, input().split()))
  N, solders = data[0], data[1:]
  solders.sort()
  
  solderNums = [0]
  results = [0]

  for idx in range(N):
    if solderNums[-1] != solders[idx]:
      solderNums.append(solders[idx])
      results.append(1)
    else:
      results[-1] += 1

  if results.count(max(results)) == 1 and max(results) > N // 2:
    print(solderNums[results.index(max(results))])
  else:
    print('SYJKGW')