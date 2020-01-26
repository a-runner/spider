# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return

import requests


link = 'http://wthrcdn.etouch.cn/weather_mini?city='

res = requests.get(link + "长春").json()
print(res)

