stack = ["ab","aa","aa","bcd","ab"]

new_stk = []

for word in stack:
    if new_stk and new_stk[-1] == word:
        new_stk.pop()
    else:
        new_stk.append(word)

print(len(new_stk))