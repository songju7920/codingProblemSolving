sticks = [64, 32, 16, 8, 4, 2, 1]
count = 0
lenSum = 0
X = int(input())

for stick in sticks:
  if lenSum + stick <= X:
    lenSum += stick
    count += 1
  if lenSum == X: break

print(count)