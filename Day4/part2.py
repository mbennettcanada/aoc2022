file_data = open("input.txt", "r").read()
pairs = file_data.split("\n")
count = 0
for pair in pairs:
    pairlist = pair.split(",")
    alist = []
    for assignment in pairlist: 
        alist.append(assignment.split("-"))
    if int(alist[0][0]) < int(alist[1][0]):
        if (int(alist[0][1]) >= int(alist[1][0])):
            count += 1
        else:
            print(alist)
    elif int(alist[0][0]) > int(alist[1][0]):
        if int(alist[1][1]) >= int(alist[0][0]):
            count +=1
        else:
            print(alist)
    else:
        count +=1

print(count)