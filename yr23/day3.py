import sys

def getnum(g: list[str], y: int, x: int) -> [(int, int)]:
    s = [(y,x)]
    f, b = (x+1, x-1)
    while f<len(g[y]) and g[y][f].isnumeric():
        s.append((y,f))
        f += 1
    while b>=0 and g[y][b].isnumeric():
        s.insert(0, (y,b))
        b -= 1
    return s

def getNeighbors(g: list[str], y: int, x: int) -> list[str]:
    ns = []
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if i==y and j==x:
                continue
            try:
                if g[i][j].isnumeric():
                    if (i,j-1) not in ns:
                        ns.append((i,j))
            except IndexError:
                continue
    return ns

g = [l.strip() for l in sys.stdin.readlines()]
tot = 0
ns = []
for i in range(1, len(g)):
    for j in range(1, len(g[i])):
        if g[i][j]!='.' and not g[i][j].isnumeric():
            ns += (getNeighbors(g, i, j))

nums = []
for y,x in ns:
    n = getnum(g, y, x)
    if n not in nums:
        nums.append(n)
for n in nums:
    tot += int("".join([g[y][x] for y,x in n]))
print(tot)