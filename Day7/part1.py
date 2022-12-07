data = open("input.txt", "r").read().split("\n")
dirmap = {}
current_dir = ['']

for line in data:
    if "$" in line:  # Yay a command
        splitline = line.split(' ')
        if splitline[1] == 'cd':
            if splitline[2] == '..':
                current_dir = current_dir[:-1]
            elif splitline[2] == '/':
                current_dir = ['']
            else:
                current_dir.append(splitline[2])
        elif splitline[1] == 'ls':
            dirmap['/'.join(current_dir)] = 0
    else:
        splitline = line.split(' ')
        if splitline[0] == 'dir':
            pass
        else:
            for i,d in enumerate(current_dir):
                dirmap['/'.join(current_dir[:i+1])] = dirmap['/'.join(current_dir[:i+1])] + int(splitline[0])
                
print(sum({k:v for (k,v) in dirmap.items() if v <= 100000}.values()))