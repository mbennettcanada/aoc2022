file_obj = open("input.txt", "r")
file_data = file_obj.read()
matches = file_data.split("\n")
total_score = 0
for match in matches:
    if match == 'A X':
        total_score = total_score + 3 #lose using scissors
    elif match == 'A Y':
        total_score = total_score + 4 #tie using rock
    elif match == 'A Z':
        total_score = total_score + 8 #win using paper
    elif match == 'B X':
        total_score = total_score + 1 #lose using rock
    elif match == 'B Y':
        total_score = total_score + 5 #tie useing paper
    elif match == 'B Z':
        total_score = total_score + 9 #win using scissors
    elif match == 'C X':
        total_score = total_score + 2 #losing using paper
    elif match == 'C Y':
        total_score = total_score + 6 #tie using scissors
    elif match == 'C Z':
        total_score = total_score + 7 #win using rock
    else: 
        print(match)

print(total_score)