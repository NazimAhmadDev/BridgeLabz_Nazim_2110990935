file_path = 'example.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    if len(lines) >= 4:
        print(lines[3])  
    else:
        print("The file has less than 4 lines.")
