import requests
import base64

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

with open('颜值排行/一半.jpg', 'rb') as f:
    data['image'] = base64.b64encode(f.read())
    response = requests.post(url, headers=headers, data=data)
    beauty = response.json()['result']['face_list'][0]['beauty']
    # beauty = response.json()
    print('韩', beauty)
