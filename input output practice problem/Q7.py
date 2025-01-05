names = input("Enter three names separated by spaces: ").split()

if len(names) == 3:
    name1, name2, name3 = names
    print(f"Name 1: {name1}")
    print(f"Name 2: {name2}")
    print(f"Name 3: {name3}")
else:
    print("Please enter exactly three names.")
