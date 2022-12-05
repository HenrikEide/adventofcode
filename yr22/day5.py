from sys import stdin
boxs = [
    ["G", "P", "N", "R"],
    ["H", "V", "S", "C", "L", "B", "J", "T"],
    ["L", "N", "M", "B", "D", "T"],
    ["B", "S", "p", "V", "R"],
    ["H", "V", "M", "W", "S", "Q", "C", "G"],
    ["J", "B", "D", "C", "S", "Q", "W"],
    ["L", "Q", "F"],
    ["V", "F", "L", "D", "T", "H", "M", "W"],
    ["F", "J", "M", "V", "B", "P", "L"]
]

ls = [x.split() for x in stdin.readlines()]
for l in ls:
    n, s, t = int(l[1]), int(l[3])-1, int(l[5])-1
    temp = boxs[s][:n]
    boxs[s] = boxs[s][n:]
    boxs[t] = temp + boxs[t]
print([x[0] for x in boxs])