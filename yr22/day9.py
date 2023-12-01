import sys
ms = [x.strip() for x in sys.stdin.readlines()]
hx, hy = 0, 0
tx, ty = 0, 0
sol = set()
for m in ms:
    direction, distance = m[0], int(m[2:])
    if direction == "U":
        hy += distance
    elif direction == "D":
        hy -= distance
    elif direction == "L":
        hx -= distance
    elif direction == "R":
        hx += distance

    if (abs(hx - tx) == 1 and abs(hy - ty) == 0) or (abs(hx - tx) == 0 and abs(hy - ty) == 1):
        tx, ty = hx, hy
    elif abs(hx - tx) == 2 and abs(hy - ty) == 0:
        tx += (hx - tx) // 2
    elif abs(hx - tx) == 0 and abs(hy - ty) == 2:
        ty += (hy - ty) // 2
    else:
        if hx < tx:
            tx -= 1
        elif hx > tx:
            tx += 1
        elif hy < ty:
            ty -= 1
        elif hy > ty:
            ty += 1
    print((tx, ty))
    sol.add((tx, ty))

print(len(sol))