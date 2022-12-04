import sys
cals = sys.stdin.read().split("\n\n")
tot = [sum(list(map(int, x.split()))) for x in cals]
print(sum(sorted(tot, reverse=True)[:3]))