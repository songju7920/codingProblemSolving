T = int(input())

for _ in range(T):
  results = input()
  answer = 0
  cnt = 1
  for result in results:
    if result == 'O':
      answer += cnt
      cnt += 1
    else:
      cnt = 1
  print(answer)