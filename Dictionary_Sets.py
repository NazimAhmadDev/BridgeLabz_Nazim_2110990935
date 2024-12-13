# Dictoinary
# (dictionary is key value pairs)
marks = {"Ragul": 100,
         "Ajay": 80,
         "Varun": 50
        }

print(marks,type(marks))

print(marks["Ajay"])

print(marks.items())

print(marks.keys())
print(marks.values())

marks.update({"Ragul":95,"Renu": 99})
print(marks.items())

score = marks.get("Ajay")
print(score)
