file_data = open("input.txt", "r").read()
instructions = file_data.split("\n")
register = 1
reg_hist = [1]

for i in instructions:
    isplit = i.split(" ")
    itype = isplit[0]
    if itype == "addx":
        inum =  int(isplit[1])
        reg_hist.append(register)
        register += inum
        reg_hist.append(register)
    else:
        reg_hist.append(register)

sigstren_list = []
for index,regval in enumerate(reg_hist):
    if (index+21)%40 == 0:
        print(f"index: {index}, value: {regval}")
        sigstren_list.append(regval*(index+1))

#print(sigstren_list)
print(sum(sigstren_list))
