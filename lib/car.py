# car.py
from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, wheel_size, wheel_number):
        super().__init__(wheel_size, wheel_number)

    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

    # The fill_up_tank method is inherited from the Vehicle class
