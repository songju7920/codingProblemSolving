n = int(input())
DP = [0] * (n + 2)
DP[0] = 0
DP[1] = -1
DP[2] = 1

for i in range(2, n + 1):
    answers = []
    if i >= 5 and DP[i - 5] != -1: answers.append(DP[i - 5] + 1)
    if DP[i - 2] != -1: answers.append(DP[i - 2] + 1)
    if len(answers) == 0: DP[i] = -1
    else: DP[i] = min(answers)

print(DP[n])