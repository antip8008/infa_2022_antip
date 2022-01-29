import turtle
turtle.shape('turtle')
turtle.shapesize(1)
turtle.color('red')
turtle.width(2)

number_of_shapes = 10

for shape in range(1, number_of_shapes+1):
    #Draw a squaere
    for step in range(4):
        turtle.forward(20 + shape * 20)
        turtle.right(90)
    #Move to position of next squaer
    turtle.penup()
    turtle.goto(-shape * 10, shape * 10)
    turtle.pendown()
turtle.done()

