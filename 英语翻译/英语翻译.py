from PIL import ImageGrab
import time
import keyboard
import cv2
from ctypes import windll, c_int
import requests
import win32api
import numpy



while True:
    # 清除剪切板
    user32 = windll.user32
    # 窗口句柄
    user32.OpenClipboard(c_int(0))
    # 清空剪切板
    user32.EmptyClipboard()
    user32.CloseClipboard()

    # 等待截图 利用qq截图
    keyboard.wait(hotkey='ctrl+alt+a')

    # 获取剪切板的内容
    while True:
        # 考虑剪切板是不是空的
        image = ImageGrab.grabclipboard()
        # 判断剪切板是不是有内容
        if image:
            break
        time.sleep(2)
            # 1.图像保存之后识别    2.直接识别图片
        # 图片格式的转换
        new_screen = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
        # 读取图片及图片的拓展名  tobytes表示拿到二进制数据
        im = cv2.imencode(".png", new_screen)[1].tobytes()
        print('开始识别截图内容')

        # 老师自己写的脚本
        word = ....
        # 翻译word的内容
        # 请求网址   进行实时翻译
        url = ''
        result = requests.post(url, data={"f":"auto","t":"auto","word":word}).json()
        # 转化成字典格式 键值对形式
        print(result)
        if 'word_mean' in result['content']:
            content = result['content']['word_mean']
        else:
            # 读取out中的值  翻译的值有可能存储在out或word_mean当中（实践）
            content = result['content']['out']
        # 0是句柄 最后一个0表示弹窗的类型 只有一个 确定的按钮
        win32api.MessageBox(0,str(content),"查询结果",0)

