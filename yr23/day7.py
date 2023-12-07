import sys
from collections import Counter
from functools import cmp_to_key

cards = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']

def getType(hand: list[str]) -> int:
    count = Counter(hand)
    jcount = count.pop('J', 0)
    maxCard = max(count, key=count.get, default='')
    for _ in range(jcount):
        count[maxCard] = min(count[maxCard]+1, 5)
    count = sorted(list(count.values())+[jcount*(not maxCard)], reverse=True)
    match count:
        case [5,*_]: return 1
        case [4,*_]: return 2
        case [3,2,*_]: return 3
        case [3,_,*_]: return 4
        case [2,2,*_]: return 5
        case [2,*_]: return 6
        case _: return 7

def compare(hand1: list[str], hand2: list[str]) -> int:
    h1, h2 = hand1[0], hand2[0]
    type1, type2 = getType(h1), getType(h2)
    if type1 != type2:
        return type2-type1
    for a, b in zip(h1, h2):
        if cards.index(a) < cards.index(b):
            return 1
        elif cards.index(a) > cards.index(b):
            return -1
    return 0

ls = [x.split() for x in sys.stdin.readlines()]
hands = sorted(ls, key=cmp_to_key(compare))
ans = 0
for i,bet in enumerate([int(x[1]) for x in hands]):
    ans += (i+1)*bet
print(ans)



# Part 1:

# import sys
# from functools import cmp_to_key

# cards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

# def getType(hand: list[str]) -> int:
#     card_count = {}
#     for card in hand:
#         if card in card_count:
#             card_count[card] += 1
#         else:
#             card_count[card] = 1
#     if 5 in card_count.values():
#         return 1
#     elif 4 in card_count.values():
#         return 2
#     elif 3 in card_count.values() and 2 in card_count.values():
#         return 3
#     elif 3 in card_count.values():
#         return 4
#     elif list(card_count.values()).count(2) == 2:
#         return 5
#     elif 2 in card_count.values():
#         return 6
#     else:
#         return 7 

# def compare(hand1: list[str], hand2: list[str]) -> int:
#     h1, h2 = hand1[0], hand2[0]
#     type1 = getType(h1)
#     type2 = getType(h2)
#     if type1 != type2:
#         return type2-type1
#     for a, b in zip(h1, h2):
#         if cards.index(a) < cards.index(b):
#             return 1
#         elif cards.index(a) > cards.index(b):
#             return -1
#     return 0

# hands = sorted([x.split() for x in sys.stdin.readlines()], key=cmp_to_key(compare))
# ans = 0
# for i,v in enumerate([x[1] for x in hands]):
#     ans += (i+1)*int(v)
# print(ans)