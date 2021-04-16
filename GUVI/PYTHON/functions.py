# def function_trial(x, y):
#    print("TRIAL PRINTING " + str(x) + str(y))

# function_trial("finding", "efficient")


def getting_input():
    a = int(input("Enter the value of A :"))
    b = int(input("Enter the value of B :"))
    addition_and_printing(a, b)


def addition_and_printing(a, b):
    print("The sum of A and B is : " + str(a+b))


getting_input()
