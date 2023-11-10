import sys

n = int(sys.stdin.readline())
stack = []

def push(num):
    stack.append(num)

def pop():
    if empty(): return -1
    return stack.pop()

def empty(): 
    return int(len(stack) == 0)

def clear():
    stack.clear()

def chack(str):
    for i in str:
        if i == '(': push(i)
        elif pop() == -1: return 'NO'
    if empty(): return 'YES'
    else: return 'NO'

for i in range(n):
    clear()
    str = list(sys.stdin.readline().rstrip())
    print(chack(str))