import turtle
turtle.shape('turtle')
turtle.shapesize(1)
turtle.color('blue')
turtle.width(2)
for step in range(12):
    for i in range(1):
        turtle.forward(100)
        turtle.left(180)
        turtle.forward(100)
        turtle.left(210)
turtle.done()
