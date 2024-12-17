from sys import stdin

xs = [x.strip() for x in stdin.readlines()]
plot = xs[0][0]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def findRegion(y, x, visited):
    region = []
    if y < 0 or y >= len(xs) or x < 0 or x >= len(xs[0]):
        return region
    if xs[y][x] != plot or (y, x) in visited:
        return region
    region.append((y, x))
    visited.add((y, x))
    for dy, dx in dirs:
        region += findRegion(y + dy, x + dx, visited)
    return region

def findPerimiter(region):
    p = []
    for y, x in region:
        for dy, dx in dirs:
            if (y + dy, x + dx) not in region:
                p.append((y, x, dy, dx))
    return p

def findSides(p):
    sp = 0
    for y, x, dy, dx in p:
        if (dy, dx) in [(0, 1), (0, -1)]:
            if (y+1, x, dy, dx) not in p:
                sp += 1
        else:
            if (y, x+1, dy, dx) not in p:
                sp += 1
    return sp

regions = []
for y, row in enumerate(xs):
    for x, p in enumerate(row):
        if any([(y, x) in r for r in regions]):
            continue
        plot = p
        regions.append(findRegion(y, x, set()))

areas = [len(r) for r in regions]
perimiters = [findPerimiter(r) for r in regions]
print(sum([a*len(p) for a, p in zip(areas, perimiters)]))
print(sum([a*findSides(p) for a, p in zip(areas, perimiters)]))

