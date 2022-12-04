import sys
tot = 0
for l in sys.stdin.readlines():
    a, x = l.split()
    t = (a,x)
    if (a,x) in [("A", "Y"), ("B", "X"), ("C", "Z")]:
        x = "X"
    elif (a,x) in [("A", "X"), ("B", "Z"), ("C", "Y")]:
        x = "Z"
    else:
        x = "Y"
    if a=="A" and x == "Y" or a=="B" and x=="Z" or a=="C" and x=="X":
        tot += 6
    elif a=="A" and x == "X" or a=="B" and x=="Y" or a=="C" and x=="Z":
        tot += 3
    
    if x=="X":
        tot +=1
    elif x=="Y":
        tot += 2
    else:
        tot += 3
print(tot)