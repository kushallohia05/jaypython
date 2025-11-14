class Dog:
    type="Mammal"

    def __init__(self, name):
        self.name=name

GoldenLabrador=Dog("Golden labrador") 
bulldog=Dog("Bulldog")
print("{} is a {}".format(GoldenLabrador.name, GoldenLabrador.type))