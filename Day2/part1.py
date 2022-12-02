file_obj = open("input.txt", "r")
file_data = file_obj.read()
matches = file_data.split("\n")
total_score = 0
for match in matches:
    if match == 'A X':
        total_score = total_score + 4 #tie + rock
    elif match == 'A Y':
        total_score = total_score + 8 #win + paper
    elif match == 'A Z':
        total_score = total_score + 3 #loss + scissors
    elif match == 'B X':
        total_score = total_score + 1 #loss + rock
    elif match == 'B Y':
        total_score = total_score + 5 #tie + paper
    elif match == 'B Z':
        total_score = total_score + 9 #win + scissors
    elif match == 'C X':
        total_score = total_score + 7 #win + rock
    elif match == 'C Y':
        total_score = total_score + 2 #loss + paper
    elif match == 'C Z':
        total_score = total_score + 6 #tie + scissors
    else: 
        print(match)

print(total_score)