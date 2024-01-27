import sys
input = sys.stdin.readline

N = int(input())
words = sorted(sorted(list(set([input().rstrip() for _ in range(N)]))), key=len)

for word in words:
  print(word)