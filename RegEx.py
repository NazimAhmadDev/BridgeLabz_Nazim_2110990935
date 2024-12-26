import re

# ^ operator for starts with

txt = "This rain in Spain"
x = re.search("^Spain",txt)

if x:
    print("Yes! we have a match")
else:
    print("No match")




# $ operator will be written after a string, it means ends with

txt = "This rain in Spain"
x = re.search("Spain$",txt)

if x:
    print("Yes! we have a match")
else:
    print("No match")




# [arn] search in a string contains a,r,n or not

txt = "This rain in Spain"
x = re.search("[arn]",txt)

if x:
    print("Yes! we have a match")
else:
    print("No match")




# [arn] search in a string contains a,r,n or not

txt = "This rain in Spain" 
x = re.search("[a-n]",txt)

if x:
    print("Yes! we have a match")
else:
    print("No match")




# [0-9] number from 0 to 9 (search for number present in string or not)

txt = "This rain in Spain"
x = re.search("[0-9]",txt)      # No match will be printed because no number is there

if x:
    print("Yes! we have a match")
else:
    print("No match")




# re.sub will replace

txt = "This rain in Spain"
x = re.sub("\s","_",txt)
print(x)