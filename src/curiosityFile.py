from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "city"])
p1 = Person(name="John", age="23", city="Mombasa")
p1.age = "38"
print(p1.age)


class Person:
    def __init__(self, name, age=None, city=None):
        self.name = name
        self.age = age if age is not None else "Unknown"
        self.city = city if city is not None else "Unknown"


p1 = Person("Alice")
p2 = Person("Alice", "24")
p3 = Person("Alice", "24", "Nairobi")

print(vars(p1))
print(vars(p2))
print(vars(p3))
