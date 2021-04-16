lists = ['car', 'bike', 'helicopter', 'yacht', 'jet']

# Lists are ordered, changeable, and allows duplicates

print(lists)

print(lists[3])

lists[2:4] = ['Replaced', 'in line 9']

print(lists[2:])

print(lists[:4])

print(lists[::-1])

lists.insert(5, "Am i the last in 17")

lists.append("i got appended in 19")

print(len(lists))

print(type(lists))

index = 0
for i in lists:
    print("Value : \" " + i + " \" Index Value : " + str(index))
    index += 1

lists.remove("car")

print(lists)
