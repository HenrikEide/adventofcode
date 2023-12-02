from sys import stdin
ls = [l.split(':')[1].split(';') for l in stdin.readlines()]
ls = [[x.strip() for x in l] for l in ls]
tot = 0
for i,l in enumerate(ls):
    g = 0
    for cs in l:
        for c in cs.split(','):
            n,c = c.split()
            n = int(n)
            match c:
                case 'blue':
                    g += n>14
                case 'green':
                    g += n>13
                case 'red':
                    g += n>12
    tot += (i+1)*(not g)
print(tot)
            