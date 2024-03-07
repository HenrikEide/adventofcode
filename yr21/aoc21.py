import sys
from numpy import transpose
nums = "92,12,94,64,14,4,99,71,47,59,37,73,29,7,16,32,40,53,30,76,74,39,70,88,55,45,17,0,24,65,35,20,63,68,89,84,33,66,18,50,38,10,83,75,67,42,3,56,82,34,90,46,87,52,49,2,21,62,93,86,25,78,19,57,77,26,81,15,23,31,54,48,98,11,91,85,60,72,8,69,6,22,97,96,80,95,58,36,44,1,51,43,9,61,41,79,5,27,28,13".split(",")
nums = [int(n) for n in nums]
boards = [[list(map(int, a.split())) for a in b] for b in list(map(lambda x: x.split("\n"), sys.stdin.read().split("\n\n")[:-1]))]


def isSolved(board : list) -> bool:
    for row in board:
        if sum(row) == -5:
            return True
    for row in transpose(board):
        if sum(row) == -5:
            return True

winner = []
weOut = False
for n in nums:
    for board in boards[:]:
        for row in board:
            for i in range(len(row)):
                if row[i] == n:
                    row[i] = -1
        if isSolved(board):
            if len(boards)==1:
                winner = board
                weOut = True
                break
            boards.remove(board)
    if weOut:
        break

winSum = 0
for row in winner:
    for x in row:
        if x > 0:
            winSum += x
print(winSum,n, "\n", winSum*n)