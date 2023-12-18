import sys

def dig(pos: (int,int), dir: str, l: int) -> [(int,int)]:
    match dir:
        case '3': return [(pos[0]-l,pos[1])]
        case '0': return [(pos[0],pos[1]+l)]
        case '1': return [(pos[0]+l,pos[1])]
        case '2': return [(pos[0],pos[1]-l)]

def findArea(points: [(int,int)]) -> float:
    n = len(points)
    area = 0.0
    for i in range(n):
        y1, x1 = points[i]
        y2, x2 = points[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)
    return abs(area) / 2.0

def findPerimeter(points: [(int,int)]) -> float:
    n = len(points)
    per = 0.0
    for i in range(n-1):
        y1,x1 = points[i]
        y2,x2 = points[i+1]
        per += abs(y2-y1+x2-x1)
    return per/2

dirs = [(x.split()[2][-2],x.split()[2][2:-2]) for x in sys.stdin.readlines()]
trench = [(0,0)]
for dir, l in dirs:
    trench += dig(trench[-1],dir,int(l,16))
print(findArea(trench)+findPerimeter(trench)+1)


# Part 1 flood fill:

# import sys
# dirs = [x.split()[:2] for x in sys.stdin.readlines()]

# def dig(pos: (int,int), dir: str, l: int) -> [(int,int)]:
#     match dir:
#         case 'U': return [(pos[0]-i,pos[1]) for i in range(1,l+1)]
#         case 'R': return [(pos[0],pos[1]+i) for i in range(1,l+1)]
#         case 'D': return [(pos[0]+i,pos[1]) for i in range(1,l+1)]
#         case 'L': return [(pos[0],pos[1]-i) for i in range(1,l+1)]

# def digInterior(trench: list[(int,int)]) -> list[(int,int)]:
#     dug = []
#     queue = [(-1,-1)]
#     while queue:
#         pos = queue.pop(0)
#         if pos not in dug:
#             dug.append(pos)
#             for dir in ['U','R','D','L']:
#                 t = dig(pos,dir,1)[0]
#                 if t not in dug+trench:
#                     queue.append(t)
#     return dug

# trench = [(0,0)]
# for dir, l in dirs:
#     trench += dig(trench[-1],dir,int(l))
# trench.pop(0)
# print(len(digInterior(trench)+trench))
