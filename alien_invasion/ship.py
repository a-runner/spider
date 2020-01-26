import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        # 设置飞船的初始位置
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获得其外界举行
        self.image = pygame.image.load('D:/python代码/大二上/alien_invasion/images/ship1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船中存储小数值
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False


    def update(self):
        # 限制飞船的移动速度  使其不能移除屏幕外
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
            # 移动速度越来越快
            self.ai_settings.ship_speed += 0.3


        # 限制飞船的移动速度  使其不能移除屏幕外
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed
            # 移动速度越来越快
            self.ai_settings.ship_speed += 0.3


        # 更新飞船的坐标位置
        self.rect.centerx = self.center


    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        '''让飞船居中'''
        self.center = self.screen_rect.centerx