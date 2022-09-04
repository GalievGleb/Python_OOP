class Person():
    """сreate homan"""

    def __init__(self, name, age, height, weight):
        """initializing the attributes of a person"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def description_person(self):
        """getting a description of a person"""
        description = self.name + ", ему " + str(self.age) + ", его рост " + str(self.height) + ", его вес " + str(
            self.weight)
        print("The new person's name is : " + description)

    def get_weight(self):
        print("The weight of our man : " + str(self.weight))


man = Person("Gleb", 12, 2, 4)
man.get_weight()