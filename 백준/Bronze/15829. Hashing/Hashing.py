L = int(input())
string = list(input())
hashedStr = 0

for i in range(L):
  hashedStr += (ord(string[i]) - 96) * (31 ** i)
print(hashedStr)