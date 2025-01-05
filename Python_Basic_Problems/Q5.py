def check_first_last(l1):
    if len(l1) > 0:
        if l1[0] == l1[-1]:
            return True
        else:
            return False


l1 = [1,2,3,4,5,1]

result = check_first_last(l1)

print(result)