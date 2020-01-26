import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
# 引入编组ship1.bmp
from pygame.sprite import Group
from game_state import Game_stats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化背景设置
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien invasion')
    # 创建play按钮
    play_button = Button(ai_settings, screen, 'play')
    # 用于存储游戏统计信息的实例
    stats = Game_stats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.creat_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏的主循环

    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            # 每次循环时重绘屏幕
            ship.update()
            gf.bullets_update(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
            gf.screen_update(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
            sb.show_score()
        else:
            gf.screen_update(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


if __name__ == '__main__':
    run_game()