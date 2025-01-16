string = "hello world"

words = string.split(" ")

rev_word = []

for word in words:
    stack = []

    for ch in word:
        stack.append(ch)
    
    reverse_word = ""
    while stack:
        reverse_word += stack.pop()

    rev_word.append(reverse_word)

print(rev_word)

