import sys
from math import ceil
patterns = [x.split("\n") for x in sys.stdin.read().split("\n\n")]

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def transpose(pattern: list) -> list:
    return ["".join(x) for x in zip(*pattern)]

def check_line(line:str) -> int:
    if is_palindrome(line):
        return ceil(len(line)/2)

def check_pattern(pttrn:list) -> int:
    if all([check_line(x) for x in pttrn]):
        return check_line(pttrn[0])

tot = 0
for pttrn in patterns:
    # Rows
    ans = 0
    print("\n".join(pttrn))
    if len(pttrn[0])%2:
        ans += check_pattern(pttrn) + 1
    elif all([check_line(x[:-1]) for x in pttrn]):
        ans += -1+check_line(pttrn[0][:-1])
    else:
        if all([check_line(x) for x in pttrn]):
            ans += check_line(pttrn[0])
    # Columns
    clms = transpose(pttrn)
    print(ans,"\n".join(clms))
    if len(clms[0])%2:
        if all([check_line(x[1:]) for x in clms]):
            ans += (1+check_line(clms[0][1:]))*100
        elif all([check_line(x[:-1]) for x in clms]):
            ans += (-1+check_line(clms[0][:-1]))*100
    else:
        if all([check_line(x) for x in clms]):
            ans += check_line(clms[0])*100
    print(ans)
    tot += ans
print(tot)