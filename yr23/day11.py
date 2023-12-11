import sys
from itertools import combinations

u = [x.strip() for x in sys.stdin.readlines()]

def expandU(u: list[str]) -> list[str]:
    li = [i for i in range(len(u)) if "#" not in u[i]]
    for j,i in enumerate(li):
        u = u[:i+j] + ["."*len(u[0])] + u[i+j:]
    u = ["".join(l) for l in list(map(list, zip(*u)))]
    li = [i for i in range(len(u)) if "#" not in u[i]]
    for j,i in enumerate(li):
        u = u[:i+j] + ["."*len(u[0])] + u[i+j:]
    return ["".join(l) for l in list(map(list, zip(*u)))]

def findGalaxies(u: list[str]) -> list[(int,int)]:
    galaxies = []
    for i,line in enumerate(u):
        for j,char in enumerate(line):
            if char == "#":
                galaxies.append((i,j))
    return galaxies

def dist(galaxy: (int,int), galaxy2: (int,int)) -> int:
    return abs(galaxy[0] - galaxy2[0]) + abs(galaxy[1] - galaxy2[1])

u = expandU(u)
gs = findGalaxies(u)
ans = 0
for g1,g2 in combinations(gs,2):
    if g1 != g2:
        ans += dist(g1,g2)
print(ans)