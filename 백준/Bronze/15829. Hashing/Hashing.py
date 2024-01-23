L = int(input())
string = list(input())
hashedStr = 0
M = 1234567891

for i in range(L):
  hashedStr += (ord(string[i]) - 96) * (31 ** i)
  hashedStr %= M
print(hashedStr)