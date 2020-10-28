''' 功能测试 '''

import pygame

pygame.init()

global_color = 0,250,250
i = 1
while i < 100:
    i += 1
    screen = pygame.display.set_mode((900, 800)) # surface 对象
    backgroud_color = 250,250,0
    screen.fill(backgroud_color)

    pygame.display.set_caption('看看，我做的！')

    my_logo = pygame.image.load('waixingren\my_logo.jpg')
    pygame.display.set_icon(my_logo)

    my_picture = pygame.image.load('waixingren\qq.jpg')
    background = my_picture.convert_alpha()
    screen.blit(background, (100, 200))

    rect_object = pygame.Rect(20,30, 20,30)
    fill_color = 250,0,250
    pygame.draw.rect(screen, fill_color, rect_object)
    
    pygame.display.update()

print(i)

j =1
while j < 200:
    j += 1
    screen.fill(global_color)
    pygame.display.update()  