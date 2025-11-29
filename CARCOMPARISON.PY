class BMW():
    def mileage(self):
        print("The mileage per litre of BMW  is 5 miles per litre")

    def maxspeed(self):
        print(" The max speed of BMW is 250 km/h") 

    def cost(self):
        print("The cost of BMW is 2.5 crores")

class Ferrari():
    def mileage(self):
        print("The mileage per litre of Ferrari is 5 miles per litre")

    def maxspeed(self):
        print(" The max speed of Ferrari is 330 km/h") 

    def cost(self):
        print("The cost of Ferrari is 4 crores")               

bmw=BMW()
ferrari=Ferrari()

for car in (bmw, ferrari):
    car.mileage()
    car.maxspeed()
    car.cost()
