names = set()
name = input("Enter name: ")
while name != "":
    names.add(name)
    name = input("Enter name: ")
    if name in names:
        print ("Existing name")
    else:
        print ("New name")
for n in names:
    print(n)