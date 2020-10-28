''' 创建Ship类'''
""" 
ship 类：
    属性： surface对象，Rect对象，初始位置，初始状态，移动速率
    方法：位置更新， 绘制在屏幕上
 """


import pygame as pg

class Ship():
    def __init__(self,screen):
        '''初始化飞船并设置初始位置与状态'''
        self.screen = screen  # 减肥飞船绘制到哪里

        # 加载飞船，调用 rect 属性
        self.image = pg.image.load('waixingren\qq.jpg').convert() #获得一个飞船的 Surface
        self.rect = self.image.get_rect() # 返回 image 对应的Rect 对象，有 Rect 对象的相应属性
        self.screen_rect = screen.get_rect()  # 返回 screen 对应的Rect对象，有相应的属性

        # 将每艘飞船放在屏幕的底部中央
        self.rect.centerx = self.screen_rect.centerx  # 飞船放在屏幕中间
        self.rect.bottom = self.screen_rect.bottom  # 飞船放在屏幕底部

        # 存储为小数（因为Rect对象属性值默认为整数）
        self.centerx = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # 飞船的初始状态，上下左右
        self.move_r = False # 向右初始值为 False, 表示不动
        self.move_l = False # 向左初始值为 False, 表示不动
        self.move_u = False # 向前初始值为 False, 表示不动
        self.move_d = False # 向后初始值为 False, 表示不动

        # 移动的速率,按一下走多远,上下左右
        self.move_r_rate = float(0.2)
        self.move_l_rate = float(0.2)
        self.move_u_rate = float(0.2)
        self.move_d_rate = float(0.2)

    def update(self):
        ''' 位置更新 '''
        # 右行方法 (注意边界)
        if self.move_r == True:
            self.centerx += self.move_r_rate

        # 左行
        if self.move_l == True:
            self.centerx -= self.move_l_rate

        # 上行
        if self.move_u == True:
            self.bottom -= self.move_u_rate

        # 下行
        if self.move_d == True:
            self.bottom += self.move_d_rate

        # 返回最新位置
        self.rect.centerx = self.centerx
        self.rect.bottom = self.bottom
        
    def blitme(self):  
        '''在屏幕 screen 指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect) # 将飞船的图像绘制在屏幕 Screen 的 self.rect 处
