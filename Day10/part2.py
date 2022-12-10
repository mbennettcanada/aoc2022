file_data = open("input.txt", "r").read()
instructions = file_data.split("\n")
register = 1
reg_hist = [1]
cycle = 1
screen = list("################################################################################################################################################################################################################################################")

for i in instructions:
    isplit = i.split(" ")
    itype = isplit[0]
    if itype == "addx":
        inum =  int(isplit[1])
        if register%40-1 <= cycle%40 and register%40+1 >=cycle%40:
            pass
        else:
            screen[cycle-1] = "."
        reg_hist.append(register)
        cycle +=1
        register += inum
        if register%40-1 <= cycle%40 and register%40+1 >=cycle%40:
            pass
        else:
            screen[cycle-1] = "."
        reg_hist.append(register)
        cycle +=1
    else:
        if register%40-1 <= cycle%40 and register%40+1 >=cycle%40:
            pass
        else:
            screen[cycle-1] = "."
        reg_hist.append(register)
        cycle +=1

print(f"{screen[0:39]}\n{screen[40:79]}\n{screen[80:119]}\n{screen[120:159]}\n{screen[160:199]}\n{screen[200:239]}\n")
#print(sigstren_list)
#print(sum(sigstren_list))
