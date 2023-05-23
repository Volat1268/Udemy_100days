with open("./file1.txt") as file1:
    file1_strings = file1.readlines()
    
with open("./file2.txt") as file2:
    file2_strings = file2.readlines()
    
file1_nums = [int(string.strip()) for string in file1_strings]
file2_nums = [int(string.strip()) for string in file2_strings]

    
common_nums = [num for num in file1_nums if num in file2_nums]

print(common_nums)

