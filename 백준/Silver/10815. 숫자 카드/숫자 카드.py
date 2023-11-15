cards = {}
answers = []

n = int(input())
intputCards = input().split()
for card in intputCards:
    cards[card] = 1

m = int(input())
targets = input().split()
for target in targets:
    answers.append(str(int(target in cards)))

print(" ".join(answers))