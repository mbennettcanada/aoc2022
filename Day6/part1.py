data = open("input.txt", "r").read()
checker = []
position = 0
for i,char in enumerate(data):
    if i > 3:
        llist = data[i-3:i]
        lset = set(llist)
        lset.add(char)
        if char in llist:
            pass
        elif len(lset) < 4:
            pass
        else:
            print(f"Signal at: {i+1}")
            break
    else: pass