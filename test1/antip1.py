import  turtle
def david():
    for step in range(6):
        turtle.begin_fill()
        for i in range(3):
            turtle.speed(10)
            turtle.forward(50)
            turtle.left(360 / 3)
        turtle.end_fill()
        turtle.forward(50)
        turtle.right(60)
if __name__ == '__main__':
    turtle.shape('turtle')
    turtle.shapesize(2)
    turtle.color('blue', 'red')
    david()
    turtle.backward(100)
    david()
    turtle.backward(100)
    david()
    turtle.forward(300)
    david()
    turtle.hideturtle()
    turtle.done()






