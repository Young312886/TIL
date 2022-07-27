class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    def __init__(self,name,species):
        self.name = name
        self.species = species
        Doggy.birth_of_dogs += 1
        Doggy.num_of_dogs += 1
    def bark(self):
        return "왈왈"
    def __del__(self):
        Doggy.num_of_dogs -= 1
    def get_status(cls):
        return f"{cls.birth_of_dogs}태어났고 {cls.num_of_dogs}마리 생존"
        

white = Doggy("white","chiwawa")
white.bark()
print(Doggy.num_of_dogs)
white.get_status()
del white
blue = Doggy("black","Dockshunt")
blue.get_status()