def prime_or_not(num):
    checker = 0
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            checker += 1
            break
    if checker == 0:
        print("Prime number")


prime_or_not(13)
