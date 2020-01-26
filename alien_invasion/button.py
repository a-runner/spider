import pygame.font


class Button():

    def __init__(self, ai_settings, screen, msg):
        '''初始化按钮的属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的大小和其他的属性
        self.width, self.height = 200, 50
        self.button_color = (0, 250, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的对象，并使其剧中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # 按钮的标签只需要处理一次
        self.pre_msg(msg)


    def pre_msg(self, msg):
        '''
        font.render 接受一个布尔参数  决定是否开启反锯齿功能（反锯齿让文本边缘变得更加平滑）
        :param msg:
        :return:
        '''
        self.image = self.font.render(msg, True, self.text_color, self.button_color)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.rect.center


    def draw_button(self):
        '''绘制一个用颜色填充的按钮  并将文本绘制上去'''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.image, self.image_rect)