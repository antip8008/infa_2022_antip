import turtle
from random import randint

number_of_turtle = 50
steps_of_the_time_number = 100
turtle.penup()
turtle.forward(200)
turtle.pendown()
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(200)
turtle.hideturtle()

pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtle)]  # создаем пул черепашек

for unit in pool:  # задаем каждой координаты, скорость, размер и угол поворот
    unit.turtlesize(0.4)
    unit.penup()
    unit.speed(randint(0, 10))
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.seth(randint(0, 360))

for i in range(steps_of_the_time_number):
    for g in range(len(pool)):
        angle1 = pool[g].heading()  # угол Г-ой молекулы
        x1, y1 = pool[g].pos()  # координаты положения Г-ой молекулы
        for h in range(len(pool)):  # перебор молекул не равных Г-той
            if g != h:
                x2, y2 = pool[h].pos()
                angle2 = pool[h].heading()
                dx = abs(x1 - x2)  # расстояние между координатами Х Г-ой и Х-ой(хетой) молекулой
                dy = abs(y1 - y2)  # расстояние между координатами У Г-ой и Х-ой молекулой
                if dx <= 3 and dy <= 3:  # если расстояние меньше 3 (попали в одну клетку с диагональю 3*sqrt(2))
                    pool[h].seth(-angle2)  # развернулась Х-ая молекула
                    pool[g].seth(-angle1)  # развернулась Г-ая молекула
                    pool[h].fd(5)  # движение на 5 вперед, чтобы выйти из клетки
                    pool[g].fd(5)  # движение на 5 вперед, чтобы выйти из клетки
        if x1 < -200 or x1 > 200:  # отскок от горизонтальных стенок
            pool[g].seth(180 - angle1)
        elif y1 < -200 or y1 > 200:  # отскок от вертикальных стенок
            pool[g].seth(-angle1)
        pool[g].fd(5)  # движение вперед на 5
turtle.done()