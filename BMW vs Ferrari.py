from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def fuel_type(self):
        pass
    
    @abstractmethod
    def max_speed(self):
        pass
    
class Bmw(Car):
    def fuel_type(self):
        print("BMW's fuel type is Gasoline")
    
    def max_speed(self):
        print("and its top speed is 250 km/h")

class Ferrari(Car):
    def fuel_type(self):
        print("\nInstead, Ferrari's fuel type is Diesel gasoline")
    
    def max_speed(self):
        print("and its top speed is 350 km/h")

BMW_car = Bmw()
Ferrari_car = Ferrari()

BMW_car.fuel_type()
BMW_car.max_speed()

Ferrari_car.fuel_type()
Ferrari_car.max_speed()