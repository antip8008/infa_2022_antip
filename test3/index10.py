import turtle


def move(point,a):
    x=t.xcor()
    y=t.ycor()
    if point == 'up':
        t.goto(x,y+a)
    elif point == 'down':
        t.goto(x,y-a)
    elif point == 'left':
        t.goto(x-a,y)
    elif point == 'right':
        t.goto(x+a,y)
    elif point == 'leftup':
        t.goto(x-a,y+a)
    elif point == 'rightup':
        t.goto(x+a,y+a)
    elif point == 'leftdown':
        t.goto(x-a,y-a)


def run(point,a):
    t.penup()
    move(point,a)
    t.pendown()

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.speed(0)
t.color('blue')
t.penup()
t.forward(100)
t.pendown()

s=int(input('Введи падла индекс:'))

j=0

while j!=1:
    u=s%10
    if s==0:
        break
    if u==0:
        move('up', 20)
        move('right', 20)
        move('down', 40)
        move('left', 20)
        move('up', 20)
    elif u == 1:
        move('rightup', 20)
        move('down', 40)
        run('left', 20)
        run('up', 20)
    elif u == 2:
        run('up', 20)
        move('right', 20)
        move('down', 20)
        move('leftdown', 20)
        move('right', 20)
        run('left', 20)
        run('up', 20)
    elif u == 3:
        run('up', 20)
        move('right', 20)
        move('leftdown', 20)
        move('right', 20)
        move('leftdown', 20)
        run('up', 20)
    elif u == 4:
        move('up', 20)
        run('right', 20)
        move('down', 40)
        run('up', 20)
        move('left', 20)
    elif u == 5:
        run('up', 20)
        run('right', 20)
        move('left', 20)
        move('down', 20)
        move('right', 20)
        move('down', 20)
        move('left', 20)
        run('up', 20)
    elif u == 6:
        run('up', 20)
        run('right', 20)
        move('leftdown', 20)
        move('right', 20)
        move('down', 20)
        move('left', 20)
        move('up', 20)
    elif u == 7:
        run('up', 20)
        move('right', 20)
        move('leftdown', 20)
        move('down', 20)
        run('up', 20)
    elif u == 8:
        move('up', 20)
        move('right', 20)
        move('down', 20)
        move('left', 20)
        move('down', 20)
        move('right', 20)
        move('up', 20)
        run('left', 20)
    elif u == 9:
        run('right', 20)
        move('left', 20)
        move('up', 20)
        move('right', 20)
        move('down', 20)
        move('leftdown', 20)
        run('up', 20)
    s = s // 10
    run('left', 40)
t.hideturtle()
turtle.done()
