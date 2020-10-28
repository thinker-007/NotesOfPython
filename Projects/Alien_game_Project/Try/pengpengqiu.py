
'''内建库(library) sys '''
import sys
# print(sys.version)
# print(sys.maxsize)
# print(sys.path)
# a=input('please enter a number:')
# sys.exit(a)

'''外部库 pygame '''
import pygame as pyg #简写


'''游戏初始化'''
#设置窗口大小，参数是2维tuple数组(width,height)
# 游戏名称
# 设置背景色:传入三维tuple (R,G,B)
pyg.init()
size = width, height = 1000, 700
speed = [2, 2]
screen = pyg.display.set_mode(size)  
pyg.display.set_caption('碰碰球')
background_color =(255,255,0)  #黄色

# 创建对象：加载游戏使用的球
ball = pyg.image.load('waixingren\qq.jpg')
ballrect = ball.get_rect()  # rect的相关属性,<rect(0, 0, 108, 116)>top, left, bottom, right
screenrect = screen.get_rect()

# 更新球球的位置
ballrect.centerx = screenrect.centerx
ballrect.bottom = screenrect.bottom

'''事件(events)循环圈loop'''
    # mouse click
    # mouse movement
    # keyboard press
    # joystick(操纵杆) action

while True:

    # 监视键盘，鼠标，操纵杆事件
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            sys.exit()  # 若监测到quit事件，则退出游戏,否则一直执行

    bullrect = ballrect.move(speed) # speed2维list
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # 每次循环重绘屏幕
    screen.fill(background_color) 

    screen.blit(ball, ballrect)

    # 让最近绘制的屏幕可见
    pyg.display.flip()

        


