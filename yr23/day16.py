import sys
grid = [x.strip() for x in sys.stdin.readlines()]

def step(grid: list[str], beam: ((int,int),(int,int))) -> (list[((int,int),(int,int))]):
    tile, dir = beam
    y,x = tile
    match grid[y][x]:
        case '/': 
            match dir:
                case (0,1): return [((y-1,x),(-1,0))]
                case (0,-1): return [((y+1,x), (1,0))]
                case (1,0): return [((y,x-1), (0,-1))]
                case (-1,0): return [((y,x+1), (0,1))]
        case '\\':
            match dir:
                case (0,1): return [((y+1,x), (1,0))]
                case (0,-1): return [((y-1,x), (-1,0))]
                case (1,0): return [((y,x+1), (0,1))]
                case (-1,0): return [((y,x-1), (0,-1))]
        case '|':
            if dir[1]:
                return [((y+1,x),(1,0)),((y-1,x),(-1,0))]
            else:
                return [((y+dir[0],x+dir[1]),dir)]
        case '-':
            if dir[0]:
                return [((y,x+1),(0,1)),((y,x-1),(0,-1))]
            else:
                return [((y+dir[0],x+dir[1]),dir)]
        case _: return [((y+dir[0],x+dir[1]),dir)]

def checkBeams(grid: list[str], visited: set, beams: list[((int,int),(int,int))]) -> list[(int,int)]:
    out = []
    for tile,dir in beams:
        y,x = tile
        if y<0 or y>=len(grid) or x<0 or x>=len(grid[0]) or (tile,dir) in visited:
            continue
        else:
            out.append((tile,dir))
    return out

curr = [((0,0),(0,1))]
eTiles = set(curr)
while curr:
    new = []
    for beam in curr:
        new += step(grid,beam)
    curr = checkBeams(grid,eTiles,new)
    eTiles.update(curr)

print(len(set([x[0] for x in list(eTiles)])))