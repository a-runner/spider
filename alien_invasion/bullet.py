import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        # 在（0，0）处设置子弹  再将其调整到正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储小数表示子弹的位置
        # 默认垂直方向移动 y轴控制垂直方向
        self.y = float(self.rect.y)

        # 设置子弹的颜色和速度
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        # 调整子弹的位置
        self.y -= self.speed_factor
        # 更新子弹的位置
        self.rect.y = self.y


    def draw_bullet(self):
        # 在屏幕上绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)

