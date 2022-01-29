import turtle
turtle.shape('turtle')
turtle.shapesize(1)
turtle.color('blue')
turtle.width(2)

A = 5      # начальная длинна
B = 10     # увеличение стороны
C = 20     # количество увеличений

for step in range(C):
    for i in range(2):
        turtle.forward(A)
        turtle.right(90)
    A += B
turtle.done()
