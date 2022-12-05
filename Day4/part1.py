file_data = open("input.txt", "r").read()
pairs = file_data.split("\n")
count = 0
for pair in pairs:
    pairlist = pair.split(",")
    alist = []
    for assignment in pairlist: 
        alist.append(assignment.split("-"))

    if (int(alist[0][0]) >= int(alist[1][0])) and (int(alist[0][1]) <= int(alist[1][1])):
        count += 1
        print(f"first fits in second: {alist}")
    elif (int(alist[1][0]) >= int(alist[0][0])) and (int(alist[1][1]) <= int(alist[0][1])):
        count += 1
        print(f"second fits in first: {alist}")
    else:
        print(f"NO FIT: {alist}")

print(count)