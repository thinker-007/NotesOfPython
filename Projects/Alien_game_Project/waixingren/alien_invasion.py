''' 游戏主程序'''

''' 导入模块 '''

import sys
import pygame as pg
from pygame.sprite import Sprite,Group
from settings import Settings 
from ship import Ship
from game_functions import *

''' 游戏初始化，界面，标题，logo '''

pg.init()

ai_setting = Settings() #初始化设置

screen = pg.display.set_mode(ai_setting.screen_size)
pg.display.set_caption('外星人入侵')
my_logo = pg.image.load('waixingren\my_logo.jpg')
pg.display.set_icon(my_logo)

''' 通过飞船类创建一艘飞船 '''
ship = Ship(screen) # 将飞船绘制到上面创建的 screen 

""" 创建编组存放子弹 """
bullets = Group()

''' 事件循环：开始游戏 '''
while True:
    #  检测事件：键盘或鼠标
    check_events(ship,screen,bullets)

    # 飞船根据事件行动并更新其位置 rect 属性
    ship.update()

    # 子弹更新位置
    bullets.update()
    for bullet in bullets.sprites():
        if bullet.rect.top == 0:
            bullets.remove(bullet)

    # 更新屏幕，并将飞船绘制在此屏幕上,显示pg.display.filp()
    update_screen(ai_setting, screen, ship, bullets)
 



