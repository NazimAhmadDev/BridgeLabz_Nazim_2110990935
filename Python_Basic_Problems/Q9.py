num = 121

rev_num = num

rev = 0
while (num!=0):
    digit = num%10
    rev = rev*10 + digit
    num //= 10

if(rev_num == rev):
    print("It is palindrome")
else:
    print("It is not palindrome")

