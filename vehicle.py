class Vehicle:
    def __init__(self, price):
        price=120
        print("The vehicle price is", price)

class Bus(Vehicle):
    def __init__(self, fare):
        fare=5
        print("The bus fare is", fare)
        