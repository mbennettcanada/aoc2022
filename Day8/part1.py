file_data = open("input.txt", "r").read()
forest = file_data.split("\n")
outside_trees = len(forest)*2 +((len(forest[0])*2)-4)
visible_inside = 0
column_forest = [[] for _ in range(len(forest[0]))]

for row_index, row in enumerate(forest):
    for column_index, column in enumerate(row):
        column_forest[column_index].append(column)

for row_index, row in enumerate(forest):
    for column_index, column in enumerate(row):        
        if row_index != 0 and row_index != len(forest)-1: ## Not the first or last row
            if column_index !=0 and column_index!=len(row)-1: ## Not first or last column
                visible_dirs = 0
                if column > max(forest[row_index][:column_index]):
                    visible_dirs += 1
                if column > max(forest[row_index][column_index+1:]):
                    visible_dirs += 1
                if column > max(column_forest[column_index][:row_index]):
                    visible_dirs += 1
                if column > max(column_forest[column_index][row_index+1:]):
                    visible_dirs += 1
                if visible_dirs > 0:
                    visible_inside +=1

print(visible_inside+outside_trees)

        
