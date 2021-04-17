
def sq(x):
    return x * x


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_of_squared_numbers = list(map(sq, numbers))
lists = map(sq, numbers)

print(list_of_squared_numbers)
print(*lists, sep=",")  # Can also be printed using for loop without using list method

print(lists)