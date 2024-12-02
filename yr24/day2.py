from sys import stdin

# Part 1
xs = [[int(x) for x in l.split()] for l in stdin.readlines()]

def safeCheck(r: list[int]) -> int:
    for i in range(1, len(r)):
        if 0 < (r[i] - r[i - 1]) < 4:
            continue
        return 0
    return 1

tot = 0
for r in xs:
    if r[0] > r[-1]:
        r = r[::-1]
    tot += safeCheck(r)
print(tot)

# Part 2
def fullCheck(r: list[int]) -> int:
    if safeCheck(r) > 0:
        return 1
    for i in range(0, len(r)):
        cp = r.copy()
        cp.pop(i)
        if safeCheck(cp) > 0:
            return 1
    return 0

tot = 0
for r in xs:
    rr = r.copy()[::-1]
    tot += fullCheck(r) or fullCheck(rr)
print(tot)
