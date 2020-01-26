import cv2
from aip import AipFace
import base64
import time
import pyttsx3

# 调用百度的aip
AppID = '17066944'
API_Key = 'aRBU2gfaqGtVCoFcFKTlcHyX'
Secret_Key = 'dqNz3WjKi36PyQ2bp3cbIZBTWlMN0UY8'
client = AipFace(AppID, API_Key, Secret_Key)

# 增加人脸
def face_add(filepath='example0.jpg', user_info="laoyang", group_id='test'):
    # 实现录入人脸 的功能
    # 开始录入脸
    image = fileopen(filepath)
    image_type = 'BASE64'
    """ 如果有可选参数 """
    options = {}
    options["user_info"] = user_info
    userid = str(int(time.time()))
    # 进行异常处理
    try:
        result = client.addUser(image, image_type, group_id, userid, options)
        # result = client.detect(image,  image_type, options)
        print(result)
        if result['error_code'] == 0:
            print('增加人脸成功')
        else:
            print('增加人脸失败')

    except Exception as e:
        print(e)

# 检测人脸
def face_search(group_id_list='test', filepath='example1.jpg'):
    # 将两张图片进行比较
    image = fileopen(filepath)
    image_type = 'BASE64'
    """ 调用人脸搜索 """
    result = client.search(image, image_type, group_id_list)
    print(result)
    if result['error_code'] == 0:
        score = result['result']['user_list'][0]['score']
        print(score)
        if score > 90:
            print('是同一个人')
            return True
        else:
            print('不是同一个人')
            return False
    else:
        print('没有注册人脸')
        return False

def fileopen(filepath):
    # 取得文件的数据
    with open(filepath, 'rb') as f:
        data = base64.b64encode(f.read())
    image = str(data, 'utf-8')
    return image


def say(data):
    # 初始化
    engine = pyttsx3.init()
    # 说中文
    engine.setProperty('voice', 'zh')
    engine.say(data)
    # 运行
    engine.runAndWait()

def main():

    cap = cv2.VideoCapture(0)
    while True:
        # 读取资源
        ret, frame = cap.read()
        # sigmaSpace = cv2.getTrackbarPos("sigmaSpace", "image")
        # 显示图片
        # src：输入图像
        # d：过滤时周围每个像素领域的直径
        # sigmaColor：在color space中过滤sigma。参数越大，临近像素将会在越远的地方mix。
        # sigmaSpace：在coordinate space中过滤sigma。参数越大，那些颜色足够相近的的颜色的影响越大。

        value = 28
        sigmaSpace = value * 3
        # 双边滤波的方法
        image_list = cv2.bilateralFilter(frame, value, value*2, sigmaSpace)
        cv2.imshow('frame', image_list)
        # cv2.imshow('frame', frame)
        k = cv2.waitKey(1) & 0xFF
        # 表示按下按键推出
        if k == ord('q'):
            break
        # 表示点击叉号推出
        if k == ord('a'):
            # 开始录入脸
            cv2.imwrite('example0.jpg', frame)
            print('开始注册你的脸')
            face_add()
        if k == ord('s'):
            # 开始验证你的脸
            # 两张照片相互对比
            cv2.imwrite('example1.jpg', frame)
            print('开始验证你的脸')
            re = face_search()
            if re:
                # 进行某些操作
                print('你现在可以进行操作了')
                say('大爷，您来了，等你好久了，你现在可以进行操作了')
            else:
                print('对不起，你没有录入人脸数据！')
                say('对不起，你没有权限')

        if cv2.getWindowProperty('frame', cv2.WND_PROP_AUTOSIZE) < 1:
            break

    # 释放摄像头
    cap.release()
    cv2.destroyAllWindows()




if __name__ == '__main__':
    main()