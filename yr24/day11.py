from sys import stdin

xs = [int(x) for x in stdin.read().split()]
distinct = set(xs)
stones = {x: xs.count(x) for x in xs}

for i in range(75):
    new = []
    pcounts = {x: stones[x] for x in distinct}
    for x in distinct:
        stones[x] = stones.get(x, 0) - pcounts.get(x, 0)
        count = pcounts.get(x, 1)
        if x == 0:
            stones[1] = stones.get(1, 0) + count
            new.append(1)
        elif len(str(x)) % 2 == 0:
            x = str(x)
            l, r = int(x[:len(x) // 2]), int(x[len(x) // 2:])
            stones[l] = stones.get(l, 0) + count
            stones[r] = stones.get(r, 0) + count
            new.extend([l, r])
        else:
            new_x = x * 2024
            stones[new_x] = stones.get(new_x, 0) + count
            new.append(new_x)
    distinct = set(new)

print(sum(stones.values()))