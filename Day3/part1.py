file_obj = open("input.txt", "r")
file_data = file_obj.read()
rucksacks = file_data.split("\n")
sum = 0
valuedict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

for r in rucksacks:
    side1 = set(r[0:int(len(r)/2)])             # set of the first half
    side2 = set(r[int(len(r)/2):int(len(r))])   # set of the second half
    diff = side1.intersection(side2)            # intersection of the two sets
    sum += valuedict[str(list(diff)[0])]        # convert that intersection to a list, then string, then find the value of that one letter

print(sum)

