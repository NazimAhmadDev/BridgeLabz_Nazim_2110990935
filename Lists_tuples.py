# LISTS AND TUPLES

#(list are mutable)

# LISTS
list = ["apple","banana","mango",30,"rahul",45.0,True]
list[0] = "Guawa"
print(list)

print(list[0:5])

print(list[0:7:2])

print(list[1:])
print(list[:7])


list.append("new_apple")
print(list)

list.insert(0,"new_mango")
print(list)


l1 = [5,2,4,3,1]
l1.reverse()
print(l1)

l1.sort()
print(l1)

l1.pop(3) # pop the element at index 3
print(l1)




# TUPLES

# tuples are immutable
a = (1,2,3,4)
print(type(a))

b = (5,6,7)

c = a + b
print(c)

print(c.count(5)) # count the occurence of given number

#repeat
repeat = a*3
print(repeat)
print(repeat.count(1))


print(len(repeat))


# check the existence of element
print(3 in repeat)

tuple = (1,2,3,4)
sliced = tuple[1:3]
print(sliced)

my_tuple = (1,2,3)
a, b, c = my_tuple
print(a,b,c) # 1, 2, 3


# PRACTICE SET
'''
fruits = []

f1 = int(input("Enter your fruit name: ")
fruits.append(f1)
f2 = int(input("Enter your fruit name: ")
fruits.append(f2)
f3 = int(input("Enter your fruit name: ")
fruits.append(f3)
f4 = int(input("Enter your fruit name: ")
fruits.append(f4)

print(fruits)
'''




'''
marks = []
s1 = int(input("Enter your marks: "))
marks.append(s1)

s2 = int(input("Enter your marks: "))
marks.append(s2)

s3 = int(input("Enter your marks: "))
marks.append(s3)

s4 = int(input("Enter your marks: "))
marks.append(s4)

marks.sort()

print(marks)
'''



# sum of element inside list
l = [1,2,3,4]
print(sum(l))



tup = (7,0,0,8,9,0)
print(tup.count(0))