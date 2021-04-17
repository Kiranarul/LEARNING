
x = lambda a: a + 20
print(x(5))

y = lambda a, b: a+b

print(y(10, 10))

# lambda function inside another function


def f1(number):
    return lambda a: a * number


doubler = f1(2)
triplet = f1(3)

print(doubler(11))
print(triplet(11))
