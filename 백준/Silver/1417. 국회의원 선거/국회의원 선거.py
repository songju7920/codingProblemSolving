import sys

cnt = int(input())
myVote = int(input())
candidates = [int(input()) for _ in range(cnt - 1)]
result = 0

if cnt == 1: 
  print(0) 
  sys.exit()

candidates.sort()
while myVote <= candidates[-1]:
  myVote += 1
  candidates[-1] -= 1
  candidates.sort()
  result += 1

print(result)