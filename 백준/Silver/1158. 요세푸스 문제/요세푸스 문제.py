[max_size, interval] = map(int, input().split())
people = [i + 1 for i in range(max_size)]
answer = [0] * max_size
next = interval - 1

for i in range(max_size):
  answer[i] = str(people[next])
  people = people[:next] + people[next + 1:]
  if len(people) != 0: next = (next + interval - 1) % len(people)

print('<' + ', '.join(answer) + '>')