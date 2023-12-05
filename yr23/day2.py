from sys import stdin
from math import prod
ls = [l.split(':')[1].split(';') for l in stdin.readlines()]
ls = [[x.strip() for x in l] for l in ls]
tot = 0
for i,l in enumerate(ls):
    g = [0,0,0]
    for cards in l:
        for card in cards.split(','):
            n,c = card.split()
            n = int(n)
            match c:
                case 'blue':
                    g[0] = max(g[0],n)
                case 'green':
                    g[1] = max(g[1],n)
                case 'red':
                    g[2] = max(g[2],n)
    tot += prod(g)
print(tot)


# Part 1:

# from sys import stdin
# ls = [l.split(':')[1].split(';') for l in stdin.readlines()]
# ls = [[x.strip() for x in l] for l in ls]
# tot = 0
# for i,l in enumerate(ls):
#     g = 0
#     for cards in l:
#         for card in cards.split(','):
#             n,c = card.split()
#             n = int(n)
#             match c:
#                 case 'blue':
#                     g += n>14
#                 case 'green':
#                     g += n>13
#                 case 'red':
#                     g += n>12
#     tot += (i+1)*(not g)
# print(tot)
            