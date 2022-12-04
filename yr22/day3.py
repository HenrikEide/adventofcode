from sys import stdin
tot = 0
lines = [x.strip() for x in stdin.readlines()]
for l in range(0, len(lines), 3):
    r1, r2, r3 = lines[l], lines[l+1], lines[l+2]
    d = ord(set.intersection(set(r1), set(r2), set(r3)).pop())
    if d > 96:
        tot += d-96
    else:
        tot += d-38
print(tot)