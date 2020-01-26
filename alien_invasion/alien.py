import pygame
from pygame.sprite import Sprite

'''
    表示单个外星人的类
'''

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        # 初始化外星人 并设置其初始位置
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人的图像 并设置其rect的图像
        '''
        convert_alpha()方法会使用透明的方法绘制前景对象，因此在加载一个有alpha通道的素材时
        （比如PNG TGA），需要使用convert_alpha()方法，当然普通的图片也是可以使用这个方法的，
        用了也不会有什么副作用。
        '''
        self.image = pygame.image.load('D:/python代码/大二上/alien_invasion/images/alien1_ship.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)


    def blit_me(self):
        # 在指定的位置绘制外星人
        self.screen.blit(self.image, self.rect)


    def update(self):
        '''
        向右移动外星人
        '''
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x


    def aliens_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True

        elif self.rect.left <= 0:
            return True


