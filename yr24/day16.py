from sys import stdin
import heapq


def get(xs, x, y):
    if x < 0 or y < 0 or x >= len(xs) or y >= len(xs[0]):
        return "#"
    return xs[x][y]


xs = [line.strip() for line in stdin.readlines()]
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def go_long(xs, start, end):
    pq = [(0, start, (1, 0))]
    visited = set()
    maze = {start: 0}
    predecessors = {start: []}

    while pq:
        cost, (x, y), dir = heapq.heappop(pq)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if (x, y) == end:
            continue

        for d in dirs:
            nx, ny = x + d[0], y + d[1]
            if get(xs, nx, ny) != "#" and (nx, ny) not in visited:
                new_cost = cost + 1 + 1000 * (dir != d)
                if (nx, ny) not in maze or new_cost < maze[(nx, ny)]:
                    maze[(nx, ny)] = new_cost
                    heapq.heappush(pq, (new_cost, (nx, ny), d))
                    predecessors[(nx, ny)] = [(x, y)]
                elif new_cost == maze[(nx, ny)]:
                    predecessors[(nx, ny)].append((x, y))
    return predecessors


def backtrack(predecessors, start, end):
    def backtrack(current):
        if current == start:
            return [[start]]
        paths = []
        for pred in predecessors[current]:
            for path in backtrack(pred):
                paths.append(path + [current])
        return paths

    return backtrack(end)


# pred = go_long(xs, (139, 1), (1, 139))
# paths = backtrack(pred, (139, 1), (1, 139))
# print(len(paths))
# print(paths)
print("Testy ")
pred = go_long(xs, (15, 1), (1, 15))
paths = backtrack(pred, (15, 1), (1, 15))
print("Length:", len(paths[0]))
print(paths)
print(go_long(xs, (25, 1), (1, 25)))
