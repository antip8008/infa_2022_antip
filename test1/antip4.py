import turtle

def circle():
    for i in range(360):
        turtle.forward(1)
        turtle.left(1)
if __name__ == '__main__':
    turtle.shape('turtle')
    turtle.color('purple')
    turtle.speed(50)
    turtle.width(5)
    circle()
    turtle.hideturtle()
turtle.done()