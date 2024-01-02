N = int(input())
players = list(map(int, input().split()))
player1 = players[0]
players = players[1:]
players.sort()

isSuccess = True
for player in players:
  if player1 > player:
    player1 += player
  else:
    isSuccess = False
    break

if isSuccess: print('Yes')
else: print('No')