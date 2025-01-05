file_path = 'example.txt'

with open(file_path, 'r') as file:
    content = file.read()
    if len(content) == 0:
        print("The file is empty.")
    else:
        print("The file is not empty.")
