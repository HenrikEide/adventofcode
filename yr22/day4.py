from sys import stdin
ls = [x.strip().split(",") for x in stdin.readlines()]
tot = 0
for n, m in ls:
    n1, n2 = [int(x) for x in n.split("-")]
    m1, m2 = [int(x) for x in m.split("-")]
    if n2 < m1 or m2 < n1:
        continue
    tot += 1
print(tot)