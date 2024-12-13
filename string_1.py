# SLICING
name = "Nazim"

print(name[0:3]) # Naz

print(name[:5])  # Nazim

print(name[-5:-1]) # Nazi

print(name[1:]) # azim

print(name[:5]) # Nazim



word = "amazing"
print(word[0:7:2]) # aaig

name = "Nazim Ahmad"
print(len(name))

print(name.endswith("N"))
print(name.startswith("N"))

#capital first letter of a string
print(name.capitalize())    # Nazim ahmad

#capital first letter of all word
print(name.title())         # Nazim Ahmad

# find 
print(name.find('i'))


# replace 
sentence = "I am very sad sad today"
print(sentence.replace('sad','happy'))



# escape sequence character
a = "Nazim is a good boy\nbut not a bad\n boy. Hello my name is\t nazim ahmad \"boy\" "

print(a)
