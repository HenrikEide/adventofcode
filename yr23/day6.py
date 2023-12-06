rs1 = [(40,215), (92,1064), (97,1505), (90,1100)]
rs2 = [(40929790,215106415051100)]
ans = 1
for t,d in rs2:
    speed = 0
    while 1:
        speed += 1
        if speed*(t-speed) > d:
            break
    ans *= t-speed*2+1

print(ans)