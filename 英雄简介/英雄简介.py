import requests
import csv
from lxml import etree

# 获取英雄名称 https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js

def get_info():
    url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"
    response = requests.get(url).json()
    data = response['hero']
    with open('lol.csv', 'w', encoding='utf-8') as f:
        f.write('name,alias,title')
        for d in data:
            name = d['name']
            alias = d['alias']
            title = d['title']
            f.write(f'\n{name},{alias},{title}')



def get_introduction():

    with open('lol.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        slugs = [r['alias'] for r in reader]
        # 'https://yz.lol.qq.com/v1/zh_cn/champions/vayne/index.json'
    print(slugs)

    for i, alias in enumerate(slugs):
        url = f'https://yz.lol.qq.com/v1/zh_cn/champions/{alias.lower()}/index.json'
        # print(url)
        response = requests.get(url).json()
        name = response['champion']['name']
        title = response['champion']['title']
        # print(title)
        biography = response['champion']['biography']
        content = ''
        for bio in biography.values():
            content += bio

        # 此时的content中含有<p>的标签   需要处理掉
        # print(content)

        # 加载字符串的内容
        html = etree.HTML(content)
        # 去除p标签
        content = html.xpath('//p/text()')
        content = '\n'.join(content)
        # print(content)

        with open('lol_story.txt', 'a', encoding='utf-8') as f:

            f.write(f'\n第{i+1}节   {name}--{title}\n')
            f.write(f'\n {content}\n')







if __name__ == '__main__':
    get_introduction()