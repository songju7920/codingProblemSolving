import sys
input = sys.stdin.readline

set_value = 0b000000000000000000000

def set_controller (commend):
  global set_value
  data = commend.split()
  if data[0] == 'add':
    set_value = set_value | (1 << int(data[1]))
  if data[0] == 'remove':
    set_value = set_value & ~(1 << int(data[1]))
  if data[0] == 'check':
    print(1 if set_value & (1 << int(data[1])) != 0 else 0)
  if data[0] == 'toggle':
    set_value = set_value ^ (1 << int(data[1]))
  if data[0] == 'all':
    set_value = 0b111111111111111111110
  if data[0] == 'empty':
    set_value = 0b000000000000000000000

N = int(input())

for _ in range(N):
  set_controller(input())