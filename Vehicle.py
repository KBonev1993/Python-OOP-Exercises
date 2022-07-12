class Vehicle:
    def __init__(self, mileage, max_speed=150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []

    def  max_speed(self):
        return self.max_speed()

    def mileage(self):
        return self.mileage()

    def gadgets(self):
        return self.gadgets()



car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
