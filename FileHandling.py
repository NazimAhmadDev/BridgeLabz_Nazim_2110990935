# File reading
f = open('demo.txt')
print(f.read())
f.close()

print("**********************************************")

f = open('demo.txt')
print(f.read(5))    # Read only 5 characters from the file
f.close()


f = open('demo.txt')
print(f.read())
f.close()



# File handling using (with). Using with operator file automatically closed

with open('demo.txt','w') as f:     # 'w' operator symbol will overwrite the content inside the file
    f.write("I am first line\n")
    f.write("I am also newline of this file.\n")



with open('demo.txt','a') as f:
    f.write("Third line is added.\n")



# creating a new file with other mode
with open('example.txt','w+') as f:
    content = f.read()
    f.write("I am the new file\n")


with open('example.txt','r+') as f:
    content = f.read()
    print(content)


print("***************************************")


with open('example.txt','w+') as f:
    f.write("New first is added")
    f.seek(0)        # seek() function will move the pointer to whatever the index we have given
    content = f.read()
    print(content)



# readline and readlines
with open('demo.txt','r') as f:
    print(f.readline())     # read one line
    print(f.readlines())    # read all lines into a list



# tell()
with open('demo.txt','r') as f:
    print(f.tell())     # current position of pointer





# creating a new file
'''
with open('new_textFile.txt','x') as f:
    f.write("This file is created using x mode")

f = open("new_textFile.txt",'r')
print(f.read())

'''




# Deleting a file
import os
if os.path.exists('Text.txt'):
    os.remove('Text.txt')
else:
    print("File does not exist")



# Renaming a file
import os
os.rename('new_textFile.txt','Text.txt')




# Reading CSV file
'''
import csv

with open('data.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
'''