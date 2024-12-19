





# FILTERS

numbers = [1,2,3,4,5]
even = filter(lambda x: x % 2 == 0,numbers)
print(list(even))


words = ["hi","hello","world","yes"]
long_word = filter(lambda x: len(x)>3,words)
print(list(long_word))


# Practice questions
words = ['apple','banana','apricot','grape','avocado']
prefix = filter(lambda x: x.startswith('a'),words)
print(list(prefix))

numbers = [10,23,45,67,50,90]
div = filter(lambda x: x % 5 == 0,numbers)
print(list(div))


numbers = [-10,25,15,-78,30,4]
neg = filter(lambda x: x<0,numbers)
print(list(neg))


words = ["hi","hello","world","yes","Python"]
char = filter(lambda x: len(x)>4,words)
print(list(char))




#check if number is prime or not
def is_prime(num):
    if(num < 2):
        return False
    for i in range(2,int(num**0.5)+1):
        if(num % i == 0):
            return False
    return True

numbers = [2,3,4,5,6,7,8,9,10]

prime_numbers = filter(is_prime,numbers)

print(list(prime_numbers))



#Check if strings are palindrome or not
def is_palindrome(word):
    return word == word[::-1]
    
words = ["madam","racecar","hello","level","world","noon"]

palindromes = filter(is_palindrome,words)

print(list(palindromes))





# Check Leap year
def leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False

years = [2000,2001,2002,2003,2004,2005,2010,2015]

leap = filter(leap_year,years)
print(list(leap))



# Valid email
emails = ["abc@gmail.com","invalid-email","user@domain","hello@world.com"]

valid_email = filter(lambda x: x.endswith(".com") or "@" in x,emails)
print((list(valid_email)))

# or
def is_valid_email(email):
    return "@" in email and email.endswith(('.com','.org','.net','.org'))

emails = ["abc@gmail.com","invalid-email","user@domain","hello@world.com","test@edu","user@site.org"]

valid_emails = filter(is_valid_email,emails)
print(list(valid_emails))




# Marks greater than or  equal to 40
def has_passed(student):
    return student["marks"] >= 40

students = [
    {"name":"Alice","marks":35},
    {"name":"Bob","marks":45},
    {"name":"Charlie","marks":50},
    {"name":"Daisy","marks":30},
]

passed_students = filter(has_passed,students)
print(list(passed_students))





# MAPS

# Syntax map(function, iterable)

# converting list of numbers to their squares
numbers = [1,2,3,4,5]
squares = map(lambda x: x**2, numbers)
print(list(squares))



# Convert list of strings to uppercase
words = ["hello","world"]
uppercase = map(str.upper,words)
print(list(uppercase))


# Adding to each number
numbers = [1,2,3,4,5]
add = map(lambda x : x + 2,numbers)
print(list(add))


# converting string to len list

words = ['apple','banana','cherry']

lengths = map(len,words)
print(list(lengths))



# temperature conversion
celsius = [0,20,37,100]

fahrenheit = map(lambda c: (c*9/5)+32,celsius)
print(list(fahrenheit))



# convert list of numeric strings to integer
num = ['1','2','3','4']

Int = map(lambda x : int(x),num)
print(list(Int))


# Add corresponding elements of two lists
num1 = [1,2,3]
num2 = [4,5,6]

result = map(lambda x,y : x+y,num1,num2)
print(list(result))




# sqauring the number and then adding it
list1 = [1,2,3,4]

square_add = map(lambda x: x**2+1,list1)
print(list(square_add))



# Validate email using map
def valid_emails(emails):
    if('@' in emails and emails.endswith('.com')):
        return True
    else:
        return False

emails = ['test@example.com','invalidemail','hello@world.com']

valid = map(valid_emails,emails)
print(list(valid))