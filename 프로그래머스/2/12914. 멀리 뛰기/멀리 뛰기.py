def solution(n):
    DpTable = [0] * (n + 2)
    DpTable[1] = 1
    DpTable[2] = 2
    for i in range(3, n + 1):
        DpTable[i] = DpTable[i - 1] + DpTable[i - 2]
    return DpTable[n] % 1234567