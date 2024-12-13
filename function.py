'''
def avg():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    average = (a+b+c)/3

    print(average)


avg() #Function call
avg()
avg()
'''




# argument based functions
def goodDay(name,ending):
    print("Good Day, "+name)
    print(ending)

goodDay("Nazim","Thankyou")
goodDay("Lavisha","Thankyou")


'''
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))
print("The factorial of this number is :",factorial(n))
'''


def greatestNumber(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    else:
        return c
    
a = 1
b = 2
c = 3

print(greatestNumber(a,b,c))