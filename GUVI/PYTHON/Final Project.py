"""
Assignment Details

Get a list of name as an input from the user and make the first letters in caps and print each word as a list

"""


def get_ip(no):
    for i in range(0, no):
        str1 = "Enter name"+str(i)
        string = input(str1)
        store_info_in_list(string)
    print(lists)


def store_info_in_list(name):
    str2 = name.capitalize()
    lists.append(str(str2))


lists = []
num = int(input("Enter the number of names: "))
get_ip(num)
