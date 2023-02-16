def bgpic(self, picname=None):
    """Set background image or return name of current backgroundimage.
    Optional argument:
    picname -- a string, name of a gif-file or "nopic".
    If picname is a filename, set the corresponding image as background.
    If picname is "nopic", delete backgroundimage, if present.
    If picname is None, return the filename of the current backgroundimage.
    Example (for a TurtleScreen instance named screen):
    >>> screen.bgpic()
    'nopic'
    >>> screen.bgpic("landscape.gif")
    >>> screen.bgpic()
    'landscape.gif'
    """
    if picname is None:
        return self._bgpicname
    if picname not in self._bgpics:
        self._bgpics[picname] = self._image(picname)
    self._setbgpic(self._bgpic, self._bgpics[picname])
    self._bgpicname = picname


# coding: utf-8
import pygame
import os
import sys
from pygame.locals import *

os.chdir('E:/星空下的告白')
os.getcwd()
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("星空之美.mp3")
# pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play()
bg_size = width, height = 300, 200
bg_rgb = (255, 255, 255)
screen1 = pygame.display.set_mode(bg_size)
pygame.display.set_caption("告白音乐")
clock = pygame.time.Clock()
pause_rect = pause_image.get_rect()
print(pause_rect.width, pause_rect.height)
pause_rect.left, pause_rect.top = (width - pause_rect.width) // 2, (height - pause_rect.height) // 2
from turtle import *
from random import random, randint

os.chdir('E:星空下的告白')
screen = Screen()
width, height = 900, 700
screen.setup(width, height)
screen.title("浪漫的流星雨")
screen.bgcolor("black")
screen.mode("logo")
screen.delay(0)
printer = Turtle()
printer.hideturtle()
printer.penup()
printer.color('red')
printer.goto(-100, -350)
printer.write("宇宙广阔(弱水三千)""\n\n", move=True, align="left", font=("Italic", 30, "bold"))
printer.goto(-50, -400)
printer.write("只寻你一颗!(只取一瓢饮!)\n\n", move=True, align="left", font=("Italic", 30, "bold"))
t = Turtle(visible=False, shape='circle')
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.setheading(-90)
t.goto(width / 2, randint(-height / 2, height / 2))
stars = []
for i in range(300):
    star = t.clone()
    s = random() / 3
    if s > 0.01 and s < 0.03:
        star.pencolor("black")
        star.fillcolor("black")
    elif s > 0.03 and s < 0.04:
        star.pencolor("lightcoral")
        star.fillcolor("lightcoral")
    elif s > 0.05 and s < 0.1:
        star.pencolor("green")
        star.fillcolor("green")
    elif s > 0.15 and s < 0.16:
        star.pencolor("yellow")
        star.fillcolor("yellow")
    elif s > 0.19 and s < 0.2:
        star.pencolor("red")
        star.fillcolor("red")
    elif s > 0.21 and s < 0.22:
        star.pencolor("purple")
        star.fillcolor("purple")
    elif s > 0.29 and s < 0.3:
        star.pencolor("darkorange")
        star.fillcolor("darkorange")
    elif s > 0.31 and s < 0.32:
        star.pencolor("red")
        star.fillcolor("yellow")
    elif s > 0.32 and s < 0.33:
        star.pencolor("yellow")
        star.fillcolor("white")
    star.shapesize(s, s)
    star.speed(int(s * 30))
    star.setx(width / 2 + randint(1, width))
    star.sety(randint(-height / 2, height / 2))
    # star.showturtle()
    stars.append(star)
i = 0
pause = False
while True:
    i += 0
    for star in stars:

        star.setx(star.xcor() - 3 * star.speed())
        if star.xcor() < -width / 2:
            star.hideturtle()
            star.setx(width / 2 + randint(1, width))
            star.sety(randint(-height / 2, height / 2))
            star.showturtle()
    if i >= 100:
        break

    # 查找队列事件
    for event in pygame.event.get():
        # 查找点击关闭窗口事件
        if event.type == QUIT:
            sys.exit
        # 查找鼠标左右击事件
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                pause = not pause
            if event.button == 3:
                pause = not pause

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pause = not pause
    screen1.fill(bg_rgb)
    if pause:
        pygame.mixer.music.pause()
        screen1.blit(pause_image, pause_rect)
    else:
        pygame.mixer.music.unpause()
        screen1.blit(play_image, pause_rect)
    pygame.display.flip()
    clock.tick(30)