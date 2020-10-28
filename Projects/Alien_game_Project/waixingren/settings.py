#创建设置类，默认属性

class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 500
        self.screen_size = (self.screen_width, self.screen_height)
        self.bg_color = (250,250,0)  #yellow
