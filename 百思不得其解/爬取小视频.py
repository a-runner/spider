import requests
# 正则表达式
import re
# 下载视频的工具包
import urllib.request
import hashlib


'''
声明全局变量 除了视频资源后还有其他的数据，
选哟筛选数据，将筛选后的数据存储到全局变量中
'''

url_name = []

def get_url():
    url = 'http://www.budejie.com/'

    # 利用requests请求数据
    html = requests.get(url).text
    # print(html)

    # 数据筛选
    url_content = re.compile(r'<div class="j-r-list-c">.*?</div>.*?/div>', re.S)
    url_contents = re.findall(url_content, html)
    for i in url_contents:
        # 进一步提取数据，包括 视频标题 和视频连接
        url_reg = r'data-original="(.*?)"'
        url_items = re.findall(url_reg, i)
        # print(url_items)
        # 提取视频标题
        if url_items:
            name_reg = re.compile(r'a href="/detail-\d{8}\.html">(.*?)</a>')
            name_items = re.findall(name_reg, i)

            for a, b in zip(name_items, url_items):
                url_name.append([a,b])
        else:
            pass

def download():
    # 异常
    for i in url_name:
        print(i[0], end='')
        print(i[1])
        try:
            urllib.request.urlretrieve(i[1], './视频/%s.gif' %
                                       (hashlib.md5(i[0].encode(encoding='UTF-8')).hexdigest()))
        except Exception as e:
            print(e)
            print("下载异常！！！")
            pass


if __name__ == '__main__':
    get_url()
    download()