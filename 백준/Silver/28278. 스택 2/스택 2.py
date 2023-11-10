import sys

n = int(sys.stdin.readline())
stack = []

def push(num):
    stack.append(num)

def pop():
    if empty(): return -1
    return stack.pop()

def top():
    if empty(): return -1
    return stack[len(stack) - 1]

def empty(): 
    return int(len(stack) == 0)

def size():
    return len(stack)


for i in range(n):
    data = sys.stdin.readline().rstrip().split(' ')
    if data[0] == '1': push(int(data[1]))
    elif data[0] == '2': print(pop())
    elif data[0] == '3': print(size())
    elif data[0] == '4': print(empty())
    elif data[0] == '5': print(top())
    else: print('정의되지 않은 명령어')