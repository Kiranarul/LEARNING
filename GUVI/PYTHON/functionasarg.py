lists = ['car', 'bike', 'scooter']


def printing(x):
    print(x*3)


def list_printing(prints, lis):
    for items in lis:
        prints(items)


list_printing(printing, lists)


lists1 = ['hello', 'iam', 'bit confused']


def i_will_print_two_times(anything):
    print(anything + " " + anything)


def caller_id(fun, life):
    for i in life:
        fun(i)


caller_id(i_will_print_two_times, lists1)

