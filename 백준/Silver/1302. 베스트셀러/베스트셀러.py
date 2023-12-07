n = int(input())
bookList = []
soldedCnt = []
results = []

for i in range(n):
  book = input()
  try:
    idx = bookList.index(book)
    soldedCnt[idx] += 1
  except:
    bookList.append(book)
    soldedCnt.append(1)

maxCnt = max(soldedCnt)
for i in range(len(bookList)):
  if soldedCnt[i] == maxCnt: results.append(bookList[i])

print(min(results))