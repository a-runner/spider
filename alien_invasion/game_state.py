import pygame
import time


class Game_stats():
    '''
    跟踪游戏的统计信息
    '''

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        # 判断游戏的运行状态
        self.game_active = False
        self.high_score = 0
        self.level = 1


    def reset_stats(self):
        '''
        初始化游戏运行期间的 统计信息
        :return: None
        '''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
