import sys
seeds, *maps = sys.stdin.read().split('\n\n')
seeds = [int(s) for s in seeds.split(':')[1].split()]
seedRanges = []
for i in range(0, len(seeds), 2):
    seedRanges.append((seeds[i], seeds[i]+seeds[i+1]))
maps = [m.split('\n')[1:] for m in maps][::-1]
maps = [[list(map(int,l.split())) for l in m] for m in maps]

def inSeedRanges(loc, seedRanges=seedRanges):
    for b,t in seedRanges:
        if b <= loc <= t:
            return True
    return False

def applyMap(loc, m):
    for line in m:
        d, s, r = line
        if d <= loc <= (d + r):
            return s + loc - d
    return loc

def applyMaps(loc, ms=maps):
    for m in ms:
        loc = applyMap(loc, m)
    return loc

loc = 0
while 1:
    curr = loc
    if inSeedRanges(applyMaps(curr)):
        break
    loc += 1

print(loc)


# Part 1:

# import sys
# seeds, *maps = sys.stdin.read().split('\n\n')
# seeds = [int(s) for s in seeds.split(':')[1].split()]
# maps = [m.split('\n')[1:] for m in maps]
# loc = 2**32
# for seed in seeds:
#     curr = seed
#     for m in maps:
#         for line in [l.split() for l in m]:
#             d, s, r = map(int, line)
#             if s <= curr <= (s + r):
#                 curr = d + curr - s
#                 break
#     loc = min(loc, curr)

# print(loc)