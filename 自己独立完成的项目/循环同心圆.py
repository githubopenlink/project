import turtle
turtle.pen()

my_colors=('red','blue','yellow','pink','green','orange')

turtle.width(5)
turtle.speed(1)

for b in range(100):
    turtle.penup()
    turtle.goto(0,-b*10)
    turtle.pendown()
    turtle.color(my_colors[b%len(my_colors)])
    turtle.circle(10+b*10)

turtle.done()    #程序执行完，窗口仍然在