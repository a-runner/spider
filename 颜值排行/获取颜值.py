import requests
import base64
import csv


def face_recognition():
    # 定义一个存放颜值的列表
    ll = []
    host = 'https://aip.baidubce.com/oauth/2.0/token?'

    tokendata={
        'grant_type': 'client_credentials',
        'client_id': 'jCmFKlft9TwO4wGRhC8fye98',
        'client_secret': 'mavTcDRK1UMCMwmm0EmQeNc9EGEdFGfp'
    }

    # 获取AccessToken
    # host = host + urlencode(tokendata)
    access_token = requests.post(host, data=tokendata).json()['access_token']
    # 对图片颜值 beauty进行获取
    url = 'https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token={}'.format(access_token)

    headers = {
        'Content - Type': 'application/json'
    }

    # 构造请求参数

    data = {
        'image': '',
        'image_type': 'BASE64',
        'face_field': 'beauty'
    }
    with open('颜值排行/单身女孩数据.csv', encoding='utf-8') as fread:
        reader = csv.DictReader(fread)
        for r in reader:
            print(r['username'])
            try:
                with open('颜值排行/images/' + '{}.png'.format(r["username"]), 'rb') as f:
                    data['image'] = base64.b64encode(f.read())
                    response = requests.post(url, headers=headers, data=data)
                    beauty = response.json()['result']['face_list'][0]['beauty']
                    ll.append([r["username"], beauty])
                    print(r["username"], beauty)

            except:
                print('出现错误！！')


    # 实现颜值排序
    print(ll)
    lll = sorted(ll, key=lambda x: x[1])

    with open('颜值排行榜.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['username', 'beauty'])
        writer.writerows(lll)


if __name__ == '__main__':
    face_recognition()