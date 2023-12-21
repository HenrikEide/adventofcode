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

def bfs(grid, start, steps=64) -> int:
    y,x = start
    visited = set()
    queue = [(x,y,0)]
    while queue:
        y,x,s = queue.pop(0)
        if s == steps:
            continue
        for dy,dx in [(0,1),(1,0),(0,-1),(-1,0)]:
            if len(grid[0]) <= (nx:=x+dx) or nx < 0 or len(grid) <= (ny:=y+dy) or ny < 0:
                continue
            if (nx,ny) in visited or get(grid, ny, nx) == '#':
                continue
            visited.add((ny,nx))
            queue.append((ny,nx,s+1))
    print(visited)
    return len(visited)

print(bfs(grid, findS(grid), 6))
        