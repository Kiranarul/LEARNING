import pickle

my_list = [1, 2, 3, 4, 5, 6, 7]

pickle_file = open("MySaves.txt", "wb")
pickle.dump(my_list, pickle_file)
pickle_file.close()

pickle_file = open("MySaves.txt", "rb")
new_dict = pickle.load(pickle_file)

print(new_dict)

