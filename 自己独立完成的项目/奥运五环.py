import turtle 
turtle.width(15)

#第一个圆
turtle.color('blue')
turtle.circle(100)

#第二个圆
turtle.color('black')
turtle.penup()
turtle.goto(220,0)
turtle.pendown()
turtle.circle(100)

#第三个圆
turtle.color('red')
turtle.penup()
turtle.goto(440,0)
turtle.pendown()
turtle.circle(100)

#第四个圆
turtle.color('yellow')
turtle.penup()
turtle.goto(110,-90)
turtle.pendown()
turtle.circle(100)

#第五个圆
turtle.color('green')
turtle.penup()
turtle.goto(330,-90)
turtle.pendown()
turtle.circle(100)

turtle.done()