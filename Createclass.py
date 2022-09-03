class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("man is created")

    def sing(self):
        print(self.name + " sing")

    def dance(self):
        print(self.name + " dance")

man = Person("Gleb", 20)
woman = Person("Regina", 19)

man.dance()
woman.sing()