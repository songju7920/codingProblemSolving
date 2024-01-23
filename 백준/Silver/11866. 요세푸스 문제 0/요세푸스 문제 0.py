N, K = map(int, input().split())

solders = list(range(1, N + 1))
next = (K - 1) % N
answer = []

while solders:
  answer.append(str(solders[next]))
  solders = solders[:next] + solders[next + 1:]
  if len(solders) > 0:
    next = (next + K - 1) % len(solders)

print('<' + ', '.join(answer) + '>')