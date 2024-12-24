# File reading
f = open('demo.txt')
print(f.read())
f.close()


f = open('demo.txt')
print(f.read(5))    # Read only 5 characters from the file
f.close()


f = open('demo.txt')
print(f.read())



# File appeding
f = open('demo.txt','a')        # a is for append in file
f.write("\nThis line is added")   # to write the content in the file

f = open('demo.txt')
print(f.read())

