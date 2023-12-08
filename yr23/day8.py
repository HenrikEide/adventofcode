import sys
from math import lcm
lr, m = sys.stdin.read().split('\n\n')
m = [l.split(" = ") for l in m.split('\n')]
locMap  = {x[0]:x[1][1:-1].split(', ') for x in m}

curr = [x for x in locMap.keys() if x[2]=='A']
dists = []
i = 0
ans = 1
while 1:
    match lr[i]:
        case 'L': curr = [locMap[x][0] for x in curr]
        case 'R': curr = [locMap[x][1] for x in curr]
    for x in curr:
        if x[2]=='Z':
            dists.append(ans)
            curr.remove(x)
    if not curr:
        break
    i = (i+1)%len(lr)
    ans += 1

print(lcm(*dists))