import sys

def findS(arr: list[str]) -> (int, int):
    for i in range(len(arr)):
        if 'S' in arr[i]:
            return (i, arr[i].index('S'))
    return (len(arr), int(arr))

def getSNeighbors(arr: list[str], s: (int,int)) -> (list[(int,int)], str):
    y, x = s
    neighbors = []
    dirs = ''
    if y > 0 and arr[y-1][x] in ['|', 'F', '7']:
        neighbors.append((y-1, x))
        dirs += 'N'
    if y < len(arr)-1 and arr[y+1][x] in ['|', 'L', 'J']:
        neighbors.append((y+1, x))
        dirs += 'S'
    if x > 0 and arr[y][x-1] in ['-', 'F', 'L']:
        neighbors.append((y, x-1))
        dirs += 'W'
    if x < len(arr[y])-1 and arr[y][x+1] in ['-', 'J', '7']:
        neighbors.append((y, x+1))
        dirs += 'E'
    return (neighbors, dirs)

def replaceS(arr: list[str], s: (int, int), dirs: str) -> list[str]:
    y,_ = s
    match dirs:
        case 'NS': t = '|'
        case 'NW': t = 'J'
        case 'NE': t = 'L'
        case 'SW': t = '7'
        case 'SE': t = 'F'
        case 'WE': t = '-'
    arr[y] = arr[y].replace('S', t)
    return arr

def getTile(arr: list[str], tile: (int, int)) -> str:
    y, x = tile
    return arr[y][x]

def strReplace(s: str, i: int, c: str) -> str:
    return s[:i] + c + s[i+1:]

def stepN(arr: list[str], tile: (int, int)) -> (int, int):
    match getTile(arr, tile):
        case '|': return (tile[0]-1, tile[1])
        case 'F': return (tile[0], tile[1]+1)
        case '7': return (tile[0], tile[1]-1)

def stepE(arr: list[str], tile: (int, int)) -> (int, int):
    match getTile(arr, tile):
        case '-': return (tile[0], tile[1]+1)
        case '7': return (tile[0]+1, tile[1])
        case 'J': return (tile[0]-1, tile[1])

def stepS(arr: list[str], tile: (int, int)) -> (int, int):
    match getTile(arr, tile):
        case '|': return (tile[0]+1, tile[1])
        case 'L': return (tile[0], tile[1]+1)
        case 'J': return (tile[0], tile[1]-1)

def stepW(arr: list[str], tile: (int, int)) -> (int, int):
    match getTile(arr, tile):
        case '-': return (tile[0], tile[1]-1)
        case 'F': return (tile[0]+1, tile[1])
        case 'L': return (tile[0]-1, tile[1])

ts = sys.stdin.readlines()
s = findS(ts)
ns, dirs = getSNeighbors(ts, s)
ts = replaceS(ts, s, dirs)
curr = ns[0]
prev = s
loop = [s]
while curr != s:
    loop.append(curr)
    tmp = curr
    match (curr[0]-prev[0], curr[1]-prev[1]):
        case (-1, 0): curr = stepN(ts, curr)
        case (0, 1): curr = stepE(ts, curr)
        case (1, 0): curr = stepS(ts, curr)
        case (0, -1): curr = stepW(ts, curr)
    prev = tmp

ans = 0
enclosed = False
f = False
l = False
for i in range(len(ts)):
    for j in range(len(ts[i])):
        t = getTile(ts, (i,j))
        if (i,j) in loop:
            match t:
                case '-': continue
                case '|': enclosed = not enclosed
                case 'F': f = True
                case 'L': l = True
                case '7': enclosed = not enclosed if l else enclosed; l, f = False, False
                case 'J': enclosed = not enclosed if f else enclosed; l, f = False, False
        else:
            ans += enclosed

print(ans)


# Part 1:

# import sys

# def findS(arr: list[str]) -> (int, int):
#     for i in range(len(arr)):
#         if 'S' in arr[i]:
#             return (i, arr[i].index('S'))
#     return (len(arr), int(arr))

# def getSNeighbors(arr: list[str], s: (int,int)) -> list[(int,int)]:
#     y, x = s
#     neighbors = []
#     if y > 0 and arr[y-1][x] in ['|', 'F', '7']:
#         neighbors.append((y-1, x))
#     if y < len(arr)-1 and arr[y+1][x] in ['|', 'L', 'J']:
#         neighbors.append((y+1, x))
#     if x > 0 and arr[y][x-1] in ['-', 'F', 'L']:
#         neighbors.append((y, x-1))
#     if x < len(arr[y])-1 and arr[y][x+1] in ['-', 'J', '7']:
#         neighbors.append((y, x+1))
#     return neighbors

# def getTile(arr: list[str], tile: (int, int)) -> str:
#     y, x = tile
#     return arr[y][x]

# def stepN(arr: list[str], tile: (int, int)) -> (int, int):
#     match getTile(arr, tile):
#         case '|': return (tile[0]-1, tile[1])
#         case 'F': return (tile[0], tile[1]+1)
#         case '7': return (tile[0], tile[1]-1)

# def stepE(arr: list[str], tile: (int, int)) -> (int, int):
#     match getTile(arr, tile):
#         case '-': return (tile[0], tile[1]+1)
#         case '7': return (tile[0]+1, tile[1])
#         case 'J': return (tile[0]-1, tile[1])

# def stepS(arr: list[str], tile: (int, int)) -> (int, int):
#     match getTile(arr, tile):
#         case '|': return (tile[0]+1, tile[1])
#         case 'L': return (tile[0], tile[1]+1)
#         case 'J': return (tile[0], tile[1]-1)

# def stepW(arr: list[str], tile: (int, int)) -> (int, int):
#     match getTile(arr, tile):
#         case '-': return (tile[0], tile[1]-1)
#         case 'F': return (tile[0]+1, tile[1])
#         case 'L': return (tile[0]-1, tile[1])

# ts = sys.stdin.readlines()
# s = findS(ts)
# prev = s
# curr = getSNeighbors(ts, s)[0]
# ans = 1
# while curr != s:
#     ans += 1
#     tmp = curr
#     match (curr[0]-prev[0], curr[1]-prev[1]):
#         case (-1, 0): curr = stepN(ts, curr)
#         case (0, 1): curr = stepE(ts, curr)
#         case (1, 0): curr = stepS(ts, curr)
#         case (0, -1): curr = stepW(ts, curr)
#     prev = tmp

# print(ans//2)