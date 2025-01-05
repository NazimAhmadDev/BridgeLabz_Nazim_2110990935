def balance_test(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

# Case 1
s1 = "Yn"
s2 = "PYnative"
print(balance_test(s1, s2))  

# Case 2
s1 = "Ynf"
s2 = "PYnative"
print(balance_test(s1, s2))  
