from sys import stdin

ms = [x.split("\n") for x in stdin.read().split("\n\n")]


def getdxdy(bttn, s=10):
    return tuple(int(x[2:]) for x in bttn[s:].split(", "))


tot = 0
for a, b, p in ms:
    a, b = [getdxdy(x) for x in [a, b]]
    p = getdxdy(p, 7)
    print("\nButton A:", a, "Button B:", b, "PrizeLoc", p)
    bps = 1
    aps = 0
    while bps * b[0] < p[0] and bps * b[1] < p[1]:
        bps += 1
    while (bps * b[0] + aps * a[0] != p[0]) and (bps * b[1] + aps * a[1] != p[1]):
        bps -= 1
        aps = 0
        while bps * b[0] + aps * a[0] < p[0] and bps * b[1] + aps * a[1] < p[1]:
            aps += 1
    if (
        bps < 0
        or (bps * b[0] + aps * a[0] != p[0])
        or (bps * b[1] + aps * a[1] != p[1])
    ):
        print("No solution", bps, aps)
        continue
    print(
        "Prss:", bps, aps, "tokens:", bps * b[0] + aps * a[0], bps * b[1] + aps * a[1]
    )
    tot += bps + aps * 3

print(tot)
