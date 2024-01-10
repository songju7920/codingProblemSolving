T = int(input())

for _ in range(T):
  height, width, num = map(int, input().split())
  room, floor = divmod(num, height)
  if floor == 0: 
    floor = height
    room -= 1
  print(str(floor) + str(room + 1).zfill(2))