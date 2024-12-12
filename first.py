print("Hello world")

name = "Nazim Ahmad"
age = 20
age = 21.0

print(name)
print(age)



# Taking user input in python
"""name = input("What is your name ? ")

print("Hello "+ name)



# Type conversion
old_age = int(input("Enter your old age: "))
new_age = old_age + 2
print(new_age)

print(float(18))"""




# Strings
name = "Nazim Ahmad"
print(name.upper())

print(name.find('Ahmad'))

print(name.replace("Ahmad", "Khan"))
print(name.replace('m','z'))

# Operator
print(5*2)
print(5**2)


# conditional statement
age = 19

if age > 18:
    print("You are adult")
    print("You can vote")
elif age < 18 and age > 3:
    print("Your are child")
    print("You cannot vote")
else:
    print("Enter valid age")

print("Thank you")



# Ranges
number = range(5)
print(number)

# while Loops
i = 1
while(i<=5):
    print(i)
    i = i+1

j=1
while(j<=5):
    print(j * "* ")
    j=j+1

print("Hemlo world")

j=5
while(j>=0):
    print(j * "* ")
    j=j-1




# for loops
for i in range(5):
    print(i)



#List

marks = [21,32,63,94]
print(marks)
print(marks[0])
print(marks[-1])

new_marks = marks[0:2]
print(new_marks)


# Append / insert
score = [20,40,30]
score.append(50)
print(score)

score.insert(0,60)
print(score)

print(40 in score)

print(len(score))