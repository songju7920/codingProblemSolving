while True:
  data = list(map(int, input().split()))
  mv = max(data)
  if mv == 0: break
  data = [datum for datum in data if datum != mv]

  if mv ** 2 == data[0] ** 2 + data[1] ** 2:
    print('right')
  else:
    print('wrong')