import sys
grid = [line.strip() for line in sys.stdin.readlines()]

def findS(grid) -> (int,int):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                return x,y

def get(grid, y, x) -> str:
    try:
        return grid[y][x]
    except IndexError:
        return '#'

def takeSteps(grid, start, steps=64) -> int:
    curr = [(start)]
    nxt = []
    for _ in range(steps):
        for x,y in curr:
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                if get(grid,y+dy,x+dx) != '#':
                    nxt.append((x+dx,y+dy))
        curr = list(set(nxt))
        nxt = []
    return len(curr)

print(takeSteps(grid, findS(grid)))
        