import pyautogui
import time
# 操作鼠标 键盘


# 1 截图
# 2 识别 黑色方块
# 3 点击
# 4 循环

# 加一个保护措施  右上角 或 左上角 就会退出程序
pyautogui.FAILSAFE = True

def test(region = (490, 675, 480, 20)):
    # 获取截取图片的点
    while True:
        # 进行截图
        im = pyautogui.screenshot(region=region)
        for i in range(4):
            print(im.getpixel((60+120*i, 20)))
            if im.getpixel((60+120*i, 20))[1] == 1:
                pyautogui.click(region[0]+60+120*i, region[1]+100)


def test2():
    while True:
        s = pyautogui.locateOnScreen('重玩.png')
        time.sleep(3)
        if s:
            print(s)
            break
    test((s[0]+250, s[1]-330, 480, 20))

if __name__ == '__main__':
    # 留下转换的时间
    time.sleep(3)
    test()