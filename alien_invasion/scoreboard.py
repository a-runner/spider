import pygame.font
from pygame.sprite import Group
from pygame.sprite import Sprite
from ship import Ship


class Scoreboard():

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats


        # 显示得分信息使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始得分图像
        self.pre_score()
        self.pre_high_score()
        self.level_display()
        self.pres_ship()


    def pres_ship(self):
        '''显示余下有多少飞船'''
        self.ships_ = Group()
        for ship_number in range(self.stats.ships_left):
            # 实例化一艘飞船
            ship1 = Ship(self.ai_settings, self.screen)
            ship1.rect.x = 10 + ship1.rect.width * ship_number
            ship1.rect.y = 10
            self.ships_.add(ship1)


    def level_display(self):
        '''显示等级'''
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom + 10


    def pre_score(self):
        '''将得分渲染成一幅图像'''
        round_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def show_score(self):
        '''显示得分'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_image, self.high_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 绘制飞船
        self.ships_.draw(self.screen)


    def pre_high_score(self):
        '''显示最高得分'''
        high_score = int(round(self.stats.high_score, -1))
        score_str = "{:,}".format(high_score)
        self.high_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.high_rect = self.high_image.get_rect()
        self.high_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = 20