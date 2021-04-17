
class Humans:
    pass


class Cars:
    def __init__(self, name, year):
        self.name = name
        self.age = year

    def methods(self):
        return self.age


h1 = Cars("MG", 2009)
print(h1.age)


class Understand:
    x = 10


g1 = Understand()
print(g1.x)


class Details:
    def __init__(self, name, roll):
        self.name = name
        self.reg = roll

    def methods(self):
        print("Hi my name is " + self.name + " my roll number is " + str(self.reg))


d1 = Details("Kiran", 113318104040)

d1.methods()
j1 = Cars("Maruti", 1999)
print(j1.methods())
