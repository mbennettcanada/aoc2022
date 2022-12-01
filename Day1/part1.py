file_obj = open("input.txt", "r")
file_data = file_obj.read()
split_data = file_data.split("\n\n")
largest_sum = 0
elfnumber = 0
for elf_index,cal_list in enumerate(split_data):
    elfsum = sum((int(x) for x in cal_list.split("\n")))
    if elfsum > largest_sum:
        largest_sum = elfsum
        elfnumber = elf_index

print(largest_sum)