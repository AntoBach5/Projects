class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity
    
    def fare(self):
        base_fare = 0.05
        total_fare = base_fare * self.seating_capacity
        
        final_fare = total_fare + (total_fare * 0.1)
        return final_fare

class Bus(Vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)

BusRide = Bus(50)
print(f"To pay: {BusRide.fare()}$")