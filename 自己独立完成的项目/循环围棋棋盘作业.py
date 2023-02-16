import turtle
turtle.pen()

turtle.width(2)
turtle.speed(1)

for n in range(19):
    turtle.penup()
    turtle.goto(-200,200-n*20)
    turtle.pendown()
    turtle.forward(360)

for m in range(19):
    turtle.penup()
    turtle.goto(-200+m*20,200)
    turtle.pendown()
    turtle.goto(-200+m*20,-160)

turtle.done()    #程序执行完，窗口仍然在