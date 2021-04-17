# Dictionaries are unordered, changeable but does not allow duplicates or overwrites duplicate keys

details = {
    "Name": "Kiran",
    "Age": 21,
    "Gender": "Male",
    "Education": ["10th", "12th", "B.E"],
    "Languages": ("English", "Tamil")
}

details.update({"Name": "Kiran A"})

details.pop("Age")

details["Nationality"] = "Indian"

print(details)

name = details["Name"]

print(name)

print(type(details))




