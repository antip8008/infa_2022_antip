import turtle
turtle.shape('turtle')
turtle.shapesize(1)
turtle.color('blue')
turtle.width(2)
turtle.speed(50)

for i in range(3600):
    turtle.forward(i * 0.001)
    turtle.left(1)
turtle.done()