import sys
dirs = [x.split()[:2] for x in sys.stdin.readlines()]

def dig(pos: (int,int), dir: str, l: int) -> [(int,int)]:
    match dir:
        case 'U': return [(pos[0]-i,pos[1]) for i in range(1,l+1)]
        case 'R': return [(pos[0],pos[1]+i) for i in range(1,l+1)]
        case 'D': return [(pos[0]+i,pos[1]) for i in range(1,l+1)]
        case 'L': return [(pos[0],pos[1]-i) for i in range(1,l+1)]

def digInterior(trench: list[(int,int)]) -> list[(int,int)]:
    dug = []
    queue = [(-1,-1)]
    while queue:
        pos = queue.pop(0)
        if pos not in dug:
            dug.append(pos)
            for dir in ['U','R','D','L']:
                t = dig(pos,dir,1)[0]
                if t not in dug+trench:
                    queue.append(t)
    return dug

trench = [(0,0)]
for dir, l in dirs:
    trench += dig(trench[-1],dir,int(l))
trench.pop(0)
print(len(digInterior(trench)+trench))