list_of_file = ["1.txt", "2.txt", "3.txt"]
list_for_sorted_files = []
for file_name in list_of_file:
    with open(file_name, 'r', encoding='utf-8') as file:
        list_of_string = file.readlines()
        number_of_string = len(list_of_string)
        list_for_sorted_files += [[number_of_string, file_name, list_of_string]]
list_for_sorted_files.sort()

with open("result.txt", 'w', encoding='utf-8') as file:
    for file_name in list_for_sorted_files:
        file.write(file_name[1]+"\n")
        file.write(str(file_name[0])+"\n")
        file.write(" ".join(file_name[2])+"\n")