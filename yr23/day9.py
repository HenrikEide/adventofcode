
import sys
ns = [[int(x) for x in line.split()] for line in sys.stdin.readlines()]

ans = 0
for his in ns:
    dif = [his]
    while any(dif[-1]):
        dif.append([0]*~-len(dif[-1]))
        for i in range(len(dif[-2])-1):
            dif[-1][i] = dif[-2][i+1] - dif[-2][i]
    dif = [x[::-1] for x in dif][::-1]
    for i in range(len(dif)-1):
        dif[i+1].append(dif[i+1][-1]-dif[i][-1])
    ans += dif[-1][-1]
print(ans)


# Part 1

# import sys
# ns = [[int(x) for x in line.split()] for line in sys.stdin.readlines()]

# ans = 0
# for his in ns:
#     dif = [his]
#     while any(dif[-1]):
#         dif.append([0]*~-len(dif[-1]))
#         for i in range(len(dif[-2])-1):
#             dif[-1][i] = dif[-2][i+1] - dif[-2][i]
#     dif = dif[::-1]
#     for i in range(len(dif)-1):
#         dif[i+1].append(dif[i+1][-1]+dif[i][-1])
#     ans += dif[-1][-1]
# print(ans)