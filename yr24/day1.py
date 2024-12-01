from sys import stdin

# Part 1
ls, rs = list(map(lambda z: sorted(list(z)), list(zip(*[(int(x.split()[0]),int(x.split()[1])) for x in stdin.readlines()]))))
tot = sum([abs(x-y) for (x,y) in zip(ls, rs)])
print(tot)

# Part 2
tot = 0
for n in ls:
    tot += n*len(list(filter(lambda x: x==n, rs)))
print(tot)