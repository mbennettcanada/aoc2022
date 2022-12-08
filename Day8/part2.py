import numpy
file_data = open("input.txt", "r").read()
forest = file_data.split("\n")
outside_trees = len(forest)*2 +((len(forest[0])*2)-4)
visible_inside = 0
column_forest = [[] for _ in range(len(forest[0]))]

visibility_forest = [[] for _ in range(len(forest[0]))]     # make a rotated columnar forest for easy row lookup of column values. 
for row_index, row in enumerate(forest):
    for column_index, column in enumerate(row):
        column_forest[column_index].append(column)

visibility_list = []
for row_index, row in enumerate(forest):
    for column_index, column in enumerate(row):        
        if row_index != 0 and row_index != len(forest)-1: ## Not the first or last row
            if column_index !=0 and column_index!=len(row)-1: ## Not first or last column
                visibility = [] ## for the four values to sit in
                ## the idea with the sections below is to find all the values to the left, right, top, and bottom of the current value that are larger or equal to it, then find the closest index
                ## in that list to the current index. Swapping forest for column_forest and swapping row for column essentially rotates the whole forest for ease of max/min calculations and not creating temp lists all over and iterating like a fool all the time.
                visibility.append(column_index-max([ n for n,i in enumerate(forest[row_index][:column_index]) if i>= forest[row_index][column_index]]+[0])) ##look left  ## append the difference between the index and the closest (max) index of anumber in the row from the index to the beginning that is greater than or equal to the index value. If no value, insert 0 and subtract that from your index location
                visibility.append(min([ n for n,i in enumerate(forest[row_index][column_index+1:]) if i>= forest[row_index][column_index]]+[len(forest[row_index][column_index+1:])-1])+1) ##look right
                visibility.append(row_index-max([ n for n,i in enumerate(column_forest[column_index][:row_index]) if i>= column_forest[column_index][row_index]]+[0])) ##look up
                visibility.append(min([ n for n,i in enumerate(column_forest[column_index][row_index+1:]) if i>= column_forest[column_index][row_index]]+[len(column_forest[column_index][row_index+1:])-1])+1) ##look down
                visibility_list.append(numpy.prod(visibility)) #product of the items in the list

print(max(visibility_list))

        
