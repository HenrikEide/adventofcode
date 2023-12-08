import sys
lr, m = sys.stdin.read().split('\n\n')
m = [l.split(" = ") for l in m.split('\n')]
d  = {x[0]:x[1][1:-1].split(', ') for x in m}
curr = [x for x in d.keys() if x[2]=='A']
print(curr)
i = 0
ans = 0
while not all([x[2]=='Z' for x in curr]):
    match lr[i]:
        case 'L': curr = [d[x][0] for x in curr]
        case 'R': curr = [d[x][1] for x in curr]
    i = (i+1)%len(lr)
    ans += 1

print(ans)