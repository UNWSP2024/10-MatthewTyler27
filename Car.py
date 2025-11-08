#Matthew Tyler
#11/7/25
#Car

class Car():
    def __init__(self, year,make,):
        self.year = year
        self.make = make
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
     return self.speed
         

vehicle = Car(2025,"Honda",)
print()
for i in range(5):
    vehicle.accelerate()
    print(vehicle.get_speed())

for i in range (5):
    vehicle.brake()
    print(vehicle.get_speed())
