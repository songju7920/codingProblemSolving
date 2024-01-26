import sys

input = sys.stdin.readline

while True:
  num = list(input().rstrip())
  if num == ['0']: break
  
  front = 0
  back = len(num) - 1
  result = 'yes'

  # 루프돌며 앞과 뒤가 다른지 체크
  for i in range(0, len(num) // 2):
    if num[front + i] != num[back - i]:
      result = 'no'
      break

  # 결과 출력
  print(result)