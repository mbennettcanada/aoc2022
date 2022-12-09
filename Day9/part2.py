file_data = open("input.txt", "r").read()
steps = file_data.split("\n")
rpos = [{'x':0,'y':0},{'x':0,'y':0},{'x':0,'y':0},{'x':0,'y':0},{'x':0,'y':0},{'x':0,'y':0},{'x':0,'y':0},{'x':0,'y':0},{'x':0,'y':0},{'x':0,'y':0}]
thist = set()
thist.add(f"{rpos[9]['x']},{rpos[9]['y']}")
thistlist = []
for step in steps:
    dir,count = step.split(' ')
    for i in range(int(count)):      ## go one at a time
        for p in range(0,9):
            if p == 0:
                if dir == 'U':
                    rpos[p]['y'] +=1
                elif dir == 'D':
                    rpos[p]['y'] -=1
                elif dir == 'R':
                    rpos[p]['x'] +=1
                elif dir == 'L':
                    rpos[p]['x'] -=1
                print(f"knot {p} moves to {rpos[p]}")
            
            xdiff = rpos[p]['x']-rpos[p+1]['x']
            ydiff = rpos[p]['y']-rpos[p+1]['y']
            
            if abs(xdiff) + abs(ydiff) > 2: 
                if rpos[p]['y'] > rpos[p+1]['y']:
                    rpos[p+1]['y'] +=1
                elif rpos[p]['y'] < rpos[p+1]['y']:
                    rpos[p+1]['y'] -=1
                if rpos[p]['x'] > rpos[p+1]['x']:
                    rpos[p+1]['x'] +=1
                elif rpos[p]['x'] < rpos[p+1]['x']:
                    rpos[p+1]['x'] -=1
            elif abs(xdiff) > 1:
                if rpos[p]['x'] > rpos[p+1]['x']:
                    rpos[p+1]['x'] +=1
                elif rpos[p]['x'] < rpos[p+1]['x']:
                    rpos[p+1]['x'] -=1
            elif abs(ydiff) > 1:
                if rpos[p]['y'] > rpos[p+1]['y']:
                    rpos[p+1]['y'] +=1
                elif rpos[p]['y'] < rpos[p+1]['y']:
                    rpos[p+1]['y'] -=1
        thist.add(f"{rpos[9]['x']},{rpos[9]['y']}")
        thistlist.append(f"{rpos[9]['x']},{rpos[9]['y']}")
print(thistlist)
print(len(thist))        
        