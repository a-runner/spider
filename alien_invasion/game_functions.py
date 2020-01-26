import sys
import pygame
from bullet import Bullet
from alien import Alien
import time


def check_down(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # 向右移动移动飞船
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        # 向右移动移动飞船
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()


def check_up(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # 向右移动移动飞船
        ship.moving_right = False
        ship.ai_settings.ship_speed = 1

    elif event.key == pygame.K_LEFT:
        # 向左移动移动飞船
        ship.moving_left = False
        ship.ai_settings.ship_speed = 1


def fire_bullet(ai_settings, screen, ship, bullets):
    # 判断是否在子弹限制数之内  是的话创建新的子弹对象
    if len(bullets) <= ai_settings.bullet_allowed:
        # 创建一个子弹  并将其加入到bullets编组中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_down(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_up(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    '''在玩家单击按钮时开始游戏'''
    button_click = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_click and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        # 隐藏光标  游戏开始时
        pygame.mouse.set_visible(False)
        # 重置游戏的统计信息
        stats.reset_stats()
        stats.game_active = True
        pygame.mouse.set_visible(False)
        # 清除外星人列表和飞船的列表
        sb.level_display()
        sb.pres_ship()
        sb.pre_high_score()
        sb.pre_score()
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def screen_update(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    # 每次循环时重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 重绘所有的子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    # 如果游戏处于非活动的状态，就绘制按钮
    if not stats.game_active:
        play_button.draw_button()
    # 让最近的屏幕绘制可见
    pygame.display.flip()


def bullets_update(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # 更新子弹的位置  并删除消失的子弹
    # 对精灵组中的每一个精灵依次调用update()方法，并且update()方法需要自己在自己定义的精灵类中去实现
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets))
    check_aliens_bullets_collision(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_aliens_bullets_collision(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # 检测是否有子弹击中了外星人
    # 如果是这样 就删除相应的外星人和子弹
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_point*len(aliens)
            sb.pre_score()
            check_high_score(stats, sb)
    if len(aliens) == 0:
        bullets.empty()
        # 检测到外星人全部消失后  删除现有的子弹并创建新的一群外星人
        ai_settings.increase_speed()
        # 提高等级
        stats.level += 1
        sb.level_display()
        creat_fleet(ai_settings, screen, ship, aliens)


def get_number_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - alien_width * 2
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x


def get_number_y(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - alien_height*3 - ship_height
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows


def creat_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + alien.rect.height*2 * row_number
    aliens.add(alien)


def creat_fleet(ai_settings, screen, ship, aliens):
    # 创建一个外星人群
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_x(ai_settings, alien.rect.width)
    number_rows = get_number_y(ai_settings, ship.rect.height, alien.rect.height)
    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
           creat_alien(ai_settings, screen, aliens, alien_number, row_number)


def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    # 更新所有外星人的位置
    aliens.update()
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.aliens_edge():
            change_fleet_edge(ai_settings, aliens)
            break


def change_fleet_edge(ai_settings, aliens):
    # 将整群外星人向下移动一段距离
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed

    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''相应外星人撞到飞船'''
    if stats.ships_left > 0:
        stats.ships_left -= 1
        # 更新记分牌
        sb.pres_ship()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人   并将其放到底端中央
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        time.sleep(1)

    else:
        stats.game_active = False
        # 重现光标
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''检查是否有外星人抵达屏幕底端'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


def check_high_score(stats, sb):
    '''检查是否有最高分诞生'''
    if stats.score >= stats.high_score:
        stats.high_score = stats.score
        sb.pre_high_score()
