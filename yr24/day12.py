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
    p = 0
    for y, x in region:
        for dy, dx in dirs:
            if (y + dy, x + dx) not in region:
                p += 1
    return p

regions = []
for y, row in enumerate(xs):
    for x, p in enumerate(row):
        if any([(y, x) in r for r in regions]):
            continue
        plot = p
        regions.append(findRegion(y, x, set()))

areas = [len(r) for r in regions]
perimiters = [findPerimiter(r) for r in regions]
print(sum([a*p for a, p in zip(areas, perimiters)]))
