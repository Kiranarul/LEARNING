
lists = ["apples", "bananas", "oranges", "kiwi"]

new_list = []

for i in lists:
    if "a" in i:
        new_list.append(i)

# List Comprehension reduces the length of the code and enhances ease of coding
new_list1 = [x for x in lists if "a" in x]

print("Conditioned List using List Comprehension: " + str(new_list1))
print("Conditioned List using for loop: " + str(new_list))
print("Original List: " + str(lists))
