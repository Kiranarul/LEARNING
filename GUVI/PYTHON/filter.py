
def prime(x):
    checker = 0
    for i in range(2, x):
        if x % i == 0:
            checker += 1
            return False
    if checker == 0:
        return True


filtering = filter(prime, range(100))

print("The prime numbers are ", list(filtering))
