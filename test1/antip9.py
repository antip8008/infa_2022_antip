import turtle
turtle.shape('turtle')
turtle.shapesize(1)
turtle.color('black')
turtle.width(2)
turtle.speed(50)

def eye():
    turtle.color('black')
    turtle.begin_fill()
    turtle.circle(13)
    turtle.end_fill()

if __name__ == '__main__':
    turtle.up()
    turtle.goto(0 , -100)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor('yellow')
    turtle.circle(100)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-35 , 25)
    turtle.down()
    eye()
    turtle.penup()
    turtle.goto(35, 25)
    turtle.down()
    eye()
    turtle.penup()
    turtle.goto(-67, -40)
    turtle.down()
    turtle.width(8)
    turtle.left(310)
    for i in range(100):
        turtle.forward(1.5)
        turtle.left(1)

turtle.hideturtle()
turtle.done()
