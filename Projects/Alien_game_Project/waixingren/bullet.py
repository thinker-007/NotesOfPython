""" 建立子弹类 """
""" 
子弹类：
    属性：Rect对象尺寸，移动速度，初始位置
    方法：位置更新，绘制在屏幕上
 """

import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen, ship): # 要将screen绘制到屏幕上所以有screen参数
        """ 基本属性值 """
        Sprite.__init__(self)
        self.screen = screen 
        self.bul_width = 3
        self.bul_height = 15
        self.bul_speed = (0,0.000005) # 只在y轴上动
        self.color = (0,0,0)
        self.rect = pg.Rect(0,0, self.bul_width, self.bul_height)
        # 子弹从飞创出发
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

    def update(self):
        """ 更新位置：rect的属性值(x, y) """
        self.rect.x -= self.bul_speed[0]
        self.rect.y -= self.bul_speed[1]

    def draw_bullet(self):
        """ 在屏幕中绘制子弹 """
        pg.draw.rect(self.screen,self.color, self.rect)

