from collections import deque

T = int(input())

for _ in range(T):
  answer = 0
  N, targetIdx = map(int, input().split())
  queue = deque(list(map(int, input().split())))
  maxValue = max(queue)

  while True:
    currunt = queue.popleft()
    targetIdx -= 1

    if maxValue == currunt:
      answer += 1
      if targetIdx == -1: break
      maxValue = max(queue)
    else:
      queue.append(currunt)
    
    if targetIdx == -1:
      targetIdx = len(queue) - 1
  
  print(answer)