file_data = open("input.txt", "r").read()
steps = file_data.split("\n")
hpos = {'x':0,'y':0}
tpos = {'x':0,'y':0}
thist = set()
thist.add(f"{tpos['x']},{tpos['y']}")

for step in steps:
    dir,count = step.split(' ')
    for i in range(int(count)):      ## go one at a time
        if dir == 'U':
            hpos['y'] +=1
        elif dir == 'D':
            hpos['y'] -=1
        elif dir == 'R':
            hpos['x'] +=1
        elif dir == 'L':
            hpos['x'] -=1
        
        xdiff = hpos['x']-tpos['x']
        ydiff = hpos['y']-tpos['y']
        diag = False
        if xdiff !=0 and ydiff !=0:
            diag = True
        
        if abs(xdiff) + abs(ydiff) > 2: ## houston we have an extended diagonal to reconcile
            if dir == 'U':
                tpos['y'] +=1
                tpos['x'] = hpos['x']
            elif dir == 'D':
                tpos['y'] -=1
                tpos['x'] = hpos['x']
            elif dir == 'R':
                tpos['x'] +=1
                tpos['y'] = hpos['y']
            elif dir == 'L':
                tpos['x'] -=1
                tpos['y'] = hpos['y']
        elif abs(xdiff) > 1:
            if dir == 'R':
                tpos['x'] +=1
            elif dir == 'L':
                tpos['x'] -=1
        elif abs(ydiff) > 1:
            if dir == 'U':
                tpos['y'] +=1
            elif dir == 'D':
                tpos['y'] -=1
        thist.add(f"{tpos['x']},{tpos['y']}")

print(len(thist))        
        