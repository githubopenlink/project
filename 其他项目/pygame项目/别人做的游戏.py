import sys
import pygame, random, time

pygame.init()

sc = pygame.display.set_mode((500, 500))
sc.fill((255, 255, 255))

pygame.display.update()

bg = pygame.image.load(r'E:\\素材\\素材\\熊猫.jpg')
sc.blit(bg,(0,0))

pygame.display.update()

all = 10

old_time = int(time.time())

font = pygame.font.SysFont('楷体', 120, True)

ran = random.randint(1, 4)

flag = 0

boom = pygame.image.load(r'E:\\素材\\素材\\卡通汽车纵向俯视图.jpeg')

while True:
    new_time = int(time.time())
    if new_time - old_time == 1:

        old_time = new_time
        all -= 1
        if all < 0:
            flag = -1
            break


    time_text = font.render(str(all), True, (255, 0, 0))
    sc.blit(time_text, (270, 210))
    pygame.display.update()

    sc.blit(bg,(0,0))

    if flag != 0:
        break


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1 and ran == 1:
                flag = 1
            elif event.key == pygame.K_2 and ran == 2:
                flag = 1
            elif event.key == pygame.K_3 and ran == 3:
                flag = 1
            elif event.key == pygame.K_4 and ran == 4:
                flag = 1
            else:
                flag = -1

if flag == 1:
    sc.fill((255, 255, 255))
    font = pygame.font.SysFont('楷体', 50, True)

    win_text = font.render("YOU WIN!", True, (255, 0, 0))
    sc.blit(win_text, (150, 200))
    pygame.display.update()
    time.sleep(2)
else:
    sc.blit(boom, (0, 0))
    pygame.display.update()
    time.sleep(2)