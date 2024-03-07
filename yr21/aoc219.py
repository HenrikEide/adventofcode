import sys
hmap = [[int(x) for x in y] for y in sys.stdin.read().split()]
w = len(hmap[0])
h = len(hmap)

def getHood(i, j) -> list:
    nebs = []
    if i-1>=0:
        nebs.append(hmap[i-1][j])
    if i+1<h:
        nebs.append(hmap[i+1][j])
    if j-1>=0:
        nebs.append(hmap[i][j-1])
    if j+1<w:
        nebs.append(hmap[i][j+1])
    return nebs

tot = 0
for i in range(h):
    for j in range(w):
        if all([hmap[i][j]<n for n in getHood(i, j)]):
            tot += hmap[i][j]+1
print(tot)
