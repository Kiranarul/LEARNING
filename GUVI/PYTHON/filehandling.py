import os

# We need to import os module for deleting a file and to check wher a file exists and so on

# f = open("new.txt", "x") for creating a new fine use x
f = open("new.txt", "w")
f.write("This is a new line")
f.close()

f = open("new.txt")
print(f.read())
f.close()

f = open("new.txt", "r")
