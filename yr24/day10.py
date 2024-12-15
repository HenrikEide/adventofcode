from sys import stdin

xs = [list(map(int, x.strip())) for x in stdin.readlines()]
theads = [(x, y) for y, row in enumerate(xs) for x, cell in enumerate(row) if cell == 0]

def get(x, y) -> int:
    try:
        return xs[y][x]
    except IndexError:
        return -1

def dfs(xs, h, p) -> list[(int, int)]:
    x, y = p
    if x < 0 or x >= len(xs[0]) or y < 0 or y >= len(xs):
        return []
    if xs[y][x] == 9:
        return [(x, y)]
    result = []
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if h == get(nx, ny):
            result.extend(dfs(xs, h + 1, (nx, ny)))
    return result

p1 = 0
p2 = 0
for s in theads:
    p1 += len(list(set(dfs(xs, 1, s))))
    p2 += len((dfs(xs, 1, s)))
print(p1, p2)
