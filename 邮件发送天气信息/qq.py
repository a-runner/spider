import requests, smtplib, time
from email.mime.text import MIMEText

data ={
    'link': 'http://wthrcdn.etouch.cn/weather_mini?city=',
    'city': '石家庄',
    'link1': 'http://open.iciba.com/dsapi/',
    'first': '小可爱 上线啦！！！',
    'last': '\r\n\r\n'
}
def getweather(city, link):
    url = link + city
    # url = data['link'] + data['city']
    resp = requests.get(url).json()
    yesterday = resp['data']['yesterday']
    forecast1 = resp['data']['forecast'][0]
    forecast2 = resp['data']['forecast'][1]
    msg = '\n' + '亲爱的 佳旺！ 今明两天天气状况是 :\n\n' + '\t' + forecast1['date'] \
          + '\t最高温：' + forecast1['high'] + '\t 最低温' + forecast1['low'] + '\t' \
          + forecast1['type'] + '  风力' + forecast1['fengli'][9:-3] + '\n\n\t' + forecast2['date'] + '\t最高温：' \
          + forecast2['high'] + '\t 最低温' + forecast2['low'] + '\t' + forecast2['type'] + '  风力' + forecast2['fengli'][9:-3]
    return msg
'''
    另一种写法：
    import json
    resp = requests.get(url)
    return json.loads(resp.text)
'''

def getword(link):
    res = requests.get(link).json()
    msg = res['content'] + '\n' + res['note']
    return str(msg)


if __name__ == '__main__':
    if (time.strftime('%Y-%m-%d', time.localtime(time.time()))==
    # getweather(data['city'], data['link'])
    msg = data['first'] + getweather(data['city'], data['link']) \
              + '\n\n' + getword(data['link1']) + data['last']
    message = """
        From: From 专属 贾维斯-刘佳旺 <1091899349@qq.com>
        To:To person <a---runner@qq.com>
        Subject:尊敬的主人，请点击查收!
        
        This is a e-mail message.""" + '\n' + msg

    send_msg = MIMEText(message)
    send_msg['Subject'] = '每日问候'
    send_msg['From'] = '刘佳旺专属 贾维斯'
    print(message)
    try:

        # 发送邮件
        smtp = smtplib.SMTP()
        smtp.connect('smtp.qq.com', 25)
        smtp.login('1091899349@qq.com', 'dnsnavjpgkvshegc')
        smtp.sendmail('1091899349@qq.com', '1091899349@qq.com', send_msg.as_string())
        print('发送成功！！！')

    except Exception as e:
        print('发送失败！！！')

    finally:

        smtp.quit()