lists = ["car", "bike", "truck"]

my_iter = iter(lists)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

strings = "Apples"

strings.upper()

mine = iter(strings)
print(next(mine))
print(next(mine))
print(next(mine))


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))


