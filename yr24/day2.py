from sys import stdin

xs = [[int(x) for x in l.split()] for l in stdin.readlines()]

# Part 1
def safeCheck(r) -> int:
    for i in range(1, len(r)):
        if 0 < (r[i] - r[i - 1]) < 4:
            continue
        return 0
    return 1

tot = 0
for row in xs:
    if row[0] > row[-1]:
        row = row[::-1]
    tot += safeCheck(row)
print(tot)

# Part 2
def fullCheck(r: list) -> int:
    if safeCheck(r):
        return 1
    for i in range(0, len(r)):
        cp = r.copy()
        cp.pop(i)
        if safeCheck(cp):
            return 1
    return 0

tot = 0
for row in xs:
    rrow = row.copy()[::-1]
    tot += fullCheck(row) or fullCheck(rrow)
print(tot)
