import turtle
turtle.bgcolor("orange")
turtle.setup(300, 400)
polygon = turtle.Turtle()
num_sides = 4
side_length = 70
angle = 360 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle) 

turtle.done()
