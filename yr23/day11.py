import sys
from itertools import combinations

u = [x.strip() for x in sys.stdin.readlines()]

def expandU(u: list[str]) -> list[str]:
    ey = [i for i in range(len(u)) if "#" not in u[i]]
    u = ["".join(l) for l in list(map(list, zip(*u)))]
    ex = [i for i in range(len(u)) if "#" not in u[i]]
    return (ey,ex)

def findGalaxies(u: list[str]) -> list[(int,int)]:
    galaxies = []
    for i,line in enumerate(u):
        for j,char in enumerate(line):
            if char == "#":
                galaxies.append((i,j))
    return galaxies

def dist(g1: (int,int), g2: (int,int), es:(list,list)) -> int:
    d = abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])
    ey, ex = es
    for i in ey:
        if g1[0] < i < g2[0] or g2[0] < i < g1[0]:
            d += 999999
    for j in ex:
        if g1[1] < j < g2[1] or g2[1] < j < g1[1]:
            d += 999999
    return d

es = expandU(u)
gs = findGalaxies(u)
ans = 0
for g1,g2 in combinations(gs,2):
    if g1 != g2:
        ans += dist(g1,g2, es)
print(ans)


# Part 1

# import sys
# from itertools import combinations

# u = [x.strip() for x in sys.stdin.readlines()]

# def expandU(u: list[str]) -> list[str]:
#     li = [i for i in range(len(u)) if "#" not in u[i]]
#     for j,i in enumerate(li):
#         u = u[:i+j] + ["."*len(u[0])] + u[i+j:]
#     u = ["".join(l) for l in list(map(list, zip(*u)))]
#     li = [i for i in range(len(u)) if "#" not in u[i]]
#     for j,i in enumerate(li):
#         u = u[:i+j] + ["."*len(u[0])] + u[i+j:]
#     return ["".join(l) for l in list(map(list, zip(*u)))]

# def findGalaxies(u: list[str]) -> list[(int,int)]:
#     galaxies = []
#     for i,line in enumerate(u):
#         for j,char in enumerate(line):
#             if char == "#":
#                 galaxies.append((i,j))
#     return galaxies

# def dist(galaxy: (int,int), galaxy2: (int,int)) -> int:
#     return abs(galaxy[0] - galaxy2[0]) + abs(galaxy[1] - galaxy2[1])

# u = expandU(u)
# gs = findGalaxies(u)
# ans = 0
# for g1,g2 in combinations(gs,2):
#     if g1 != g2:
#         ans += dist(g1,g2)
# print(ans)