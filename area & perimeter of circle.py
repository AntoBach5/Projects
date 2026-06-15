class circles():
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159265359
    
    def area(self):
        return self.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * self.pi * self.radius
   
question = input("Do you want to calculate the area or perimeter of your circle? (area/perimeter): ").lower()

if question == "area":
    radius_enter = float(input("Enter the radius of your circle: "))
    circle_selected = circles(radius_enter)
    print(f"The AREA of your circle is: {circle_selected.area()}") 

if question == "perimeter":
    radius_enter = float(input("Enter the radius of your circle: "))
    circle_selected = circles(radius_enter)
    print(f"The PERIMETER of your circle is: {circle_selected.perimeter()}") 