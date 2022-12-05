import re
file_data = open("input.txt", "r").read()
instructions = file_data.split("\n")
stacks = [[],['S','T','H','F','W','R'],['S','G','D','Q','W'],['B','T','W'],['D','R','W','T','N','Q','Z','J'],['F','B','H','G','L','V','T','Z'],['L','P','T','C','V','B','S','G'],['Z','B','R','T','W','G','P'],['N','G','M','T','C','J','R'],['L','G','B','W']]
for i in instructions:
    sults = re.search(r"move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)",i)
    stacks[int(sults.group(3))].extend(stacks[int(sults.group(2))][-int(sults.group(1)):])
    del stacks[int(sults.group(2))][-int(sults.group(1)):]

print(stacks)