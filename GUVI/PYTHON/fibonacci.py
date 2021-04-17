fib = [0, 1]


def get_ip():
    x = int(input("Enter the nth value :"))
    return x


def fibonacci(number):
    rep = number
    len1 = len(fib)
    fib.append(int(fib[len1-2] + fib[len1-1]))
    if len1 == number:
        print(fib[:len1])
        print(*fib[:len1], sep=", ")  # To print without brackets
    else:
        fibonacci(rep)


fibonacci(get_ip())


