seq = input().split(',')

def hash(s:str) -> int:
    curr = 0
    for c in s:
        curr += ord(c)
        curr *= 17
        curr %= 256
    return curr

boxs = [{} for _ in range(256)]
for s in seq:
    match list(s):
        case [*s,"=",n]:
            s = "".join(s)
            boxs[hash(s)][s] = int(n)
        case [*s,"-"]:
            s = "".join(s)
            boxs[hash(s)].pop(s, None)

ans = 0
for i,box in enumerate(boxs):
    for j,l in enumerate(box.items()):
        ans += (i+1)*(j+1)*int(l[1])
print(ans)

# Part 1:
# seq = input().split(',')

# def hash(s:str) -> int:
#     curr = 0
#     for c in s:
#         curr += ord(c)
#         curr *= 17
#         curr %= 256
#     return curr

# ans = 0
# for s in seq:
#     print(hash(s[:2]))
# print(ans)