from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time



class Taobao_info():
    def __init__(self):
        # 属性  登录页网址
        url = 'https://login.taobao.com/member/login.jhtml '
        self.url = url

        # 声明浏览器的驱动 括号里面加上 驱动路径（如果没有添加到环境配置的话）
        self.brower = webdriver.Chrome()
        # 等待加载
        self.wait = WebDriverWait(self.brower, 10)


    def taobao_login(self):
        # 打开网页
        self.brower.get(self.url)
        if self.brower.find_element_by_link_text('密码登录'):
            self.brower.find_element_by_link_text('密码登录').click()

        # 进行第三方登录  微博登录
        if self.brower.find_element_by_xpath('//*[@id="J_OtherLogin"]/a[1]'):
            self.brower.find_element_by_xpath('//*[@id="J_OtherLogin"]/a[1]').click()

        # 选定 账号输入框
        if self.brower.find_element_by_xpath('//*[@id="pl_login_logged"]/div/div[2]/div/input'):
            weibo_user = self.brower.find_element_by_xpath('//*[@id="pl_login_logged"]/div/div[2]/div/input')
            # 发送 输入的账号
            weibo_user.send_keys('账号')


        # 选定密码输入框
        if self.brower.find_element_by_xpath('//*[@id="pl_login_logged"]/div/div[3]/div/input'):
            weibo_pwd = self.brower.find_element_by_xpath('//*[@id="pl_login_logged"]/div/div[3]/div/input')
            weibo_pwd.send_keys('密码')

    def pay_bill(self):
        # 选中购物车节点
        if self.brower.find_element_by_xpath('//*[@id="mc-menu-hd"]'):
            self.brower.find_element_by_xpath('//*[@id="mc-menu-hd"]').click()

        # 选中商品
        if self.brower.find_element_by_xpath('//*[@id="J_Item_1428358921483"]/ul/li[1]/div/div/label'):
            self.brower.find_element_by_xpath('//*[@id="J_Item_1428358921483"]/ul/li[1]/div/div/label').click()

        # 进行产品结算
        if self.brower.find_element_by_xpath('//*[@id="J_Go"]'):
            self.brower.find_element_by_xpath('//*[@id="J_Go"]').click()

        # 点击 提交订单
        if self.brower.find_element_by_xpath('//*[@id="submitOrderPC_1"]/div/a[2]'):
            self.brower.find_element_by_xpath('//*[@id="submitOrderPC_1"]/div/a[2]').click()

'''
        之后进行付款即可
        之后再利用time设置 时间
        考虑随机误差,需要提前启动程序
'''

# 实例化的类的对象
taobao = Taobao_info()
taobao.taobao_login()