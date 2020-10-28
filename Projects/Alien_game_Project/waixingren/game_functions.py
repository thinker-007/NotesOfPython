''' 存储按键-事件函数 '''

''' 
1.定义键盘事件：
    keydown: 飞船上下左右移动，子弹发射
    keyup : 飞船停止移动
2.更新屏幕：
    重新屏幕
    将飞船绘制到更新后的位置
    将子弹绘制到更新后的位置
    展示屏幕
'''

import sys
import pygame as pg
from pygame.sprite import Sprite,Group
from ship import Ship
from bullet import Bullet

def check_keydown_events(event, screen, ship, bullets):
    if event.key == pg.K_RIGHT:  # 键盘右行按键 ‘>’
         # 调用 Ship 中右行方法
        ship.move_r = True

    elif event.key == pg.K_LEFT:  # 键盘左行按键'<'
        # 调用 Ship 中右行方法
        ship.move_l = True

    elif event.key == pg.K_UP:  # 键盘上行按键
         # 调用 Ship 中右行方法
        ship.move_u = True

    elif event.key == pg.K_DOWN:  # 键盘下行按键
         # 调用 Ship 中右行方法
        ship.move_d = True

    elif event.key == pg.K_SPACE:
        # 创建一颗子弹，并加入到编组中
        new_bullet = Bullet(screen,ship)
        bullets.add(new_bullet)

    elif event.key == pg.K_ESCAPE:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pg.K_RIGHT:  # 键盘右行按键 ‘>’
         # 调用 Ship 中右行方法
        ship.move_r = False

    elif event.key == pg.K_LEFT:  # 键盘左行按键'<'
        # 调用 Ship 中右行方法
        ship.move_l = False

    elif event.key == pg.K_UP:  # 键盘上行按键
         # 调用 Ship 中右行方法
        ship.move_u = False

    elif event.key == pg.K_DOWN:  # 键盘下行按键
         # 调用 Ship 中右行方法
        ship.move_d = False  

def check_events(ship, screen, bullets):
    ''' 响应按键和鼠标 '''
    for event in pg.event.get():
        if event.type == pg.QUIT:  
            sys.exit()  
     
        if event.type == pg.KEYDOWN:
            check_keydown_events(event, screen, ship, bullets)

        if event.type == pg.KEYUP:
            check_keyup_events(event, ship)
            
def update_screen(ai_setting, screen,ship,bullets):
    ''' 更新屏幕中的图像，并切换到新屏幕 '''
    # 清除屏幕并用纯色，setting的背景颜色属性，填充屏幕
    screen.fill(ai_setting.bg_color)  

    # 将坦克图像绘制在屏幕中的更新的Rect对象里
    ship.blitme()  

    # 将子弹绘制在屏幕里
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 展示出来
    pg.display.flip()