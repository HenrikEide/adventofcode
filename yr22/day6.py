ls = input().strip()
for i in range(len(ls)):
    if len(set(ls[i:i+14]))==14:
        print(i+14)
        break