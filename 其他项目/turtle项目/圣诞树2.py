import turtle
from turtle import *
import pygame
from pygame import *
import random

n=10
turtle.setup(700, 700, 0, 0)
turtle.speed("fastest")
turtle.screensize(bg='black')
turtle.left(90)
turtle.forward(3 * n)
turtle.color("orange", "yellow")
turtle.begin_fill()
turtle.left(126)

for i in range(5):
    turtle.forward(n / 5)
    turtle.right(144)
    turtle.forward(n / 5)
    turtle.left(72)
turtle.end_fill()
turtle.right(126)
turtle.color("dark green")
turtle.backward(n * 4.8)

def tree(d, s):
    if d <= 0: return
    turtle.forward(s)
    tree(d - 1, s * .8)
    turtle.right(120)
    tree(d - 3, s * .5)
    turtle.right(120)
    tree(d - 3, s * .5)
    turtle.right(120)
    turtle.backward(s)
tree(15, n)



bg_img = r"E:\\素材\\素材\\游戏宇宙背景.jpeg"

bg_size = (640, 640)
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("雪夜圣诞树")
bg = pygame.image.load(bg_img)

snow_list = []
for i in range(150):
    x_site = random.randrange(0, bg_size[0])   # 雪花圆心位置
    y_site = random.randrange(0, bg_size[1])   # 雪花圆心位置
    X_shift = random.randint(-1, 1)         # x 轴偏移量
    radius = random.randint(4, 6)           # 半径和 y 周下降量
    snow_list.append([x_site, y_site, X_shift, radius])

track = pygame.mixer.music.load(r'E:\\素材\\素材\\植物大战背景音乐.mp3')  # 加载音乐文件
pygame.mixer.music.play() # 播放音乐流
pygame.mixer.music.fadeout(600000)  # 设置音乐结束时间

for i in range(len(snow_list)):
        # 绘制雪花，颜色、位置、大小
        pygame.draw.circle(screen, (255, 255, 255), snow_list[i][:2], snow_list[i][3] - 3)
        # 移动雪花位置（下一次循环起效）
        snow_list[i][0] += snow_list[i][2]
        snow_list[i][1] += snow_list[i][3]
        # 如果雪花落出屏幕，重设位置
        if snow_list[i][1] > bg_size[1]:
            snow_list[i][1] = random.randrange(-50, -10)
            snow_list[i][0] = random.randrange(0, bg_size[0])
    # 刷新屏幕

turtle.done()