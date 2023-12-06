rstest = [(7,9), (15,40), (30,200)]
rs1 = [(40,215), (92,1064), (97,1505), (90,1100)]
rs2 = [(40929790,215106415051100)]
ans = 1
for t,d in rs2:
    start, end = 0,t
    while 1:
        start += 1
        if start*(t-start) > d:
            break
    while 1:
        end -= 1
        if end*(t-end) > d:
            break
    ans *= end-start+1
    
print(ans)