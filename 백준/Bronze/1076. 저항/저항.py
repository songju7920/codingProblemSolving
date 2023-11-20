colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
result = 0

target = colors.index(input())
result += target * 10
target = colors.index(input())
result += target
target = colors.index(input())
for i in range(target):
    result *= 10

print(result)