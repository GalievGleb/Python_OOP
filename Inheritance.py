class Person():
    """create human"""

    def __init__(self, name, age, height):
        """initializing the attributes of a person"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """getting a description of a person"""
        description = self.name + ", him " + str(self.age) + ", his height " + str(self.height) + ", his weight " + str(
            self.weight)
        print("The new person's name is : " + description)

    def update_weight(self, kg):
        """Human weight change"""
        self.weight = kg


class Warrior(Person):
    """Creating the war class"""

    def __init__(self, name, age, height):
        """Initialize the attributes classes of the parent"""
        super().__init__(name, age, height)
        self.rage = 500

    def get_rage(self):
        """Getting a rage charge is equal to"""
        print("the charge of rage is equal to : " + str(self.rage))

    def description_person(self):
        """Overriding the parent's method"""
        description = self.name + ", him " + str(self.age) + ", his charge of rage " + str(self.rage)
        # print("The new person's name is : " + description)
        return description


warrior = Warrior("Conan", 32, 200)
# warrior.get_rage()
# warrior.update_weight(120)
# warrior.description_person()
print("The new person's name is : " + warrior.description_person())
man = Person("Gleb", 12, 2)
man.description_person()
# man.weight = 110
# man.update_weight(120)
# man.get_weight()
