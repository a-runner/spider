class Settings():
    # 存储 游戏 中的所有设置

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1

        '''
        创建宽3像素   高15像素的子弹
        子弹速度为一
        '''
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (100, 60, 60)

        # 限制最大子弹数量
        self.bullet_allowed = 5

        # 设置外星人的移动速度
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # direction为1表示向右移动  -1表示向左移动
        self.fleet_direction = 1

        # 设置飞船的数量
        self.ship_limit = 3

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.alien_point = 50
        self.score_scale = 1.5
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        '''初始化随着游戏的进行而变化的设置'''
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.alien_point = 50
        self.fleet_direction = 1


    def increase_speed(self):
        '''提高速度设置'''
        self.alien_speed_factor *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
        self.alien_point *= int(self.score_scale)
        print(self.alien_point)

