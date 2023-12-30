N = int(input())
nums = [input() for _ in range(N)]
newNums = [''] * N
answer = 0

while len(set(newNums)) != N:
  answer += 1
  for i in range(N):
    newNums[i] += nums[i][-1 * answer]

print(answer)