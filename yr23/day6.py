part1 = [(40,215), (92,1064), (97,1505), (90,1100)]
part2 = [(40929790,215106415051100)]
ans = 1
for t,d in part2:
    v = 1
    while v*(t-v) <= d:
        v += 1
    ans *= t-v*2+1

print(ans)