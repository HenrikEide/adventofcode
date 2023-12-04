import sys
cards = [l.split(':')[1].split('|') for l in sys.stdin.readlines()]
tot = [1]*len(cards)
for i,card in enumerate(cards):
    w,h = [x.split() for x in card]
    score = sum([n in h for n in w])
    for j in range(i+1, i+score+1):
        tot[j] += tot[i]
print(sum(tot))