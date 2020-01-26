import os
# 导入时间包
from time import time
# 爬虫包
import requests
from bs4 import BeautifulSoup
# 队列  保证信息完整 先进先出
from queue import Queue

# 多线程
from threading import Thread


# 爬虫程序

# https://fabiaoqing.com/biaoqing/lists/page/1.html
'''
    数字表示 页数
'''


class Download(Thread):
    # 重写构造函数

    def __init__(self, queue, path):
        Thread.__init__(self)
        self.queue = queue
        self.path = path

        # 判断当前路径下有没有这个文件夹  如果没有就重新创建文件夹
        if not os.path.exists(path):
            os.mkdir(path)


    def run(self):
        while True:
            url = self.queue.get()
            try:
                download(url, self.path)
            finally:
                # 后续调用 告诉队列   任务处理时完整的
                self.queue.task_done()



# 爬虫程序
def download(url, path):
    # 传入两个参数  网站地址和下载路径

    response = requests.get(url)
    # 获取数据
    soup = BeautifulSoup(response.content, 'lxml')

    imag_list = soup.find_all('img', class_='ui image lazy')

    for imag in imag_list:
        # 获取图片网址
        im = imag.get('data-original')
        title = imag.get('title')
        print('下载图片', title)
        try:

            # splitext 将文件名拓展名分开
            with open(path + title + os.path.splitext(im)[-1], 'wb') as f:
                img = requests.get(im).content
                f.write(img)

        except Exception as e:
            print('图片下载失败！！')
            break


if __name__ == '__main__':
    start = time()

    # 构建所有的链接
    _url = 'https://fabiaoqing.com/biaoqing/lists/page/{page}.html'
    urls = [_url.format(page=page) for page in range(1, 201)]

    path = './表情包/'
    # 初始化线程
    queue = Queue()
    # 创建教程
    for x in range(10):
        # 创建10和线程
        worker = Download(queue, path)

        # 设置守护进程 当主线程退出时守护线程推出
        worker.daemon = True
        worker.start()

    # 将图片源地址加到队列当中
    for url in urls:
        queue.put(url)


    queue.join()

    print('下载完毕', time() - start)