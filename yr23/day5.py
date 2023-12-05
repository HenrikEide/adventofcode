import sys
seeds, *maps = sys.stdin.read().split('\n\n')
seeds = [int(s) for s in seeds.split(':')[1].split()]
newSeeds = []
for i in range(0, len(seeds), 2):
    newSeeds.extend(range(seeds[i], seeds[i]+seeds[i+1]))
print(len(newSeeds))
maps = [m.split('\n')[1:] for m in maps]
loc = 2**32
for seed in newSeeds:
    curr = seed
    for m in maps:
        for line in [l.split() for l in m]:
            d, s, r = map(int, line)
            if s <= curr <= (s + r):
                curr = d + curr - s
                break
    loc = min(loc, curr)

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