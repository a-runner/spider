from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


webdriver = webdriver.Chrome()
try:
    webdriver.get('https://cos.99.com/act/buy/xb/')
    webdriver.execute_script('window.open()')
    print(webdriver.window_handles)
    webdriver.switch_to.window(webdriver.window_handles[1])
    webdriver.get('https://www.taobao.com/')
    time.sleep(1)
    webdriver.switch_to.window(webdriver.window_handles[0])
    time.sleep(1)
    webdriver.back()
    # input = webdriver.find_element_by_id('kw')
    # input.send_keys('英魂之刃')
    # input.send_keys(Keys.ENTER)
    # wait = WebDriverWait(webdriver, 10)
    # wait.until(EC.presence_of_element_located((By.ID, 'video')))
    # # input_p = webdriver.find_elements_by_xpath('//div[@cont_b clearfix]//div[@class=info]//div[@id=meta]//p')
    # input_p = webdriver.find_elements_by_xpath('//*[@id="meta"]//p')
    # print(input_p)
    # with open('英魂之刃.txt', 'w', encoding='utf-8') as f:
    #     for i in input_p:
    #         print(i.text.strip())
    #         f.write(i.text.strip() + '\n')
    # print(webdriver.current_url)
    # print(webdriver.get_cookies())
    # # print(webdriver.page_source)
except Exception as e:
    print(e)
    print('出现错误！！')

finally:
    webdriver.close()