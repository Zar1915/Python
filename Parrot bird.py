class Parrot:
    species = "bird"
    def __init__(self, name , age):
        self.name = name
        self.age = age

Blu = Parrot("Blu" , 10)
Woo = Parrot("Woo", 10)
 
print("Blu is the {}".format(Blu.species))
print("Woo is the {}".format(Woo.species))

print("Blu is {}".format(Blu.age))
print("Woo is {}".format(Woo.age))

