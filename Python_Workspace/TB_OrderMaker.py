#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import selenium
import datetime as dt
import time
import getpass

'''
selenium实例化的browser，对应的find_element*方法，如果无法找到对应的元素，并非返回False，而是直接抛出NoSuchElementException。
因此find_element*方法放在while中进行逻辑判断会导致程序无法正常运行。
需要在while中嵌入try...except处理。
同时，即使能够找到可点击的元素，也需留0.1s以上的时间给程序和网页进行交互，否则会出现程序正常但网页未成功点击的情况。
'''

class TB_order():
    def __init__(self):
        self.__snapSleep = 0.01
        self.__shortSleep = 0.1
        self.__longSleep = 1
        self.__enoughSleep = 3

    def changeSleep(self, snaptime, shorttime, longtime, enoughtime):
        self.__snapSleep = snaptime
        self.__shortSleep = shorttime
        self.__longSleep = longtime
        self.__enoughSleep = enoughtime

    def showSleep(self):
        print('''
        SnapTime = {} seconds
        ShortTime = {} seconds
        LongTime = {} seconds
        EnoughTime = {} seconds'''.format(self.__snapSleep, 
        self.__shortSleep, 
        self.__longSleep, 
        self.__enoughSleep))

    def interactive(self):
        print('欢迎使用！当前时间 {}'.format(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        print('程序启动中，请勿关闭此界面...')
        '''
        FIXME:目前大型网站都升级了JS检测，如果识别出使用selenium.webdriver则全部判定为机器人，参考资料提出的解决方法是使用代理绕行
        因此目前输入用户名密码登录功能暂时无法实现
        print('请选择扫描二维码登录或使用用户名密码登录...')
        login_method = input('扫描二维码登录请输入0，使用密码登录请输入1（默认使用二维码登录）：')
        if login_method == '1':
            user_name = input('请输入用户名：')
            user_password = getpass.getpass('请输入密码：')
            time.sleep(__shortSleep)
            print('目前无法使用用户名密码登录')
        else:
            print('请准备扫描二维码...')
            time.sleep(__longSleep)
        '''
        self.isTest = input('请确认是否进入测试模式(Y/N)...')
        if self.isTest[0].upper() == 'N':
            order_time = input('请输入目标下单时间，格式为 YYYY-MM-DD HH:MM:SS：')
            order_time = dt.datetime.strptime(order_time, '%Y-%m-%d %H:%M:%S')
        else:
            print('测试模式启动，不会确认订单...')
            order_time = dt.datetime.now() + dt.timedelta(minutes = 1)
            print('下单时间为：{}'.format(order_time))
        return order_time

    # 启动webdriver
    def webDriver(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()

    def login(self, use_password = '0', user_name = 'user_name', user_password = 'user_password'):
        self.browser.get('https://www.taobao.com')
        time.sleep(self.__enoughSleep)

        self.browser.find_element_by_link_text("亲，请登录").click()
        time.sleep(self.__longSleep)
        current_url = self.browser.current_url

        if use_password == '1':
            try:
                self.browser.find_element_by_css_selector(".login-box.no-longlogin.module-static")
            except:
                self.browser.find_element_by_css_selector(".login-box.no-longlogin.module-quick")
                self.browser.find_element_by_id("J_Quick2Static").click()
            input_user = self.browser.find_element_by_id("TPL_username_1")
            input_user.clear()
            input_user.send_keys(user_name)
            time.sleep(self.__longSleep)
            input_password = self.browser.find_element_by_id("TPL_password_1")
            input_password.clear()
            input_password.send_keys(user_password)
            time.sleep(self.__enoughSleep)
            while True:
                try:
                    button = self.browser.find_element_by_id("nc_1_n1z")
                    action = ActionChains(self.browser)
                    action.drag_and_drop_by_offset(button, 350, 0).perform()
                    time.sleep(self.__shortSleep)
                    self.browser.find_element_by_id("J_SubmitStatic").submit()
                    break
                except:
                    time.sleep(self.__longSleep)
        else:
            try:
                self.browser.find_element_by_css_selector(".login-box.no-longlogin.module-quick")
            except:
                self.browser.find_element_by_css_selector(".login-box.no-longlogin.module-static")
                '''
                FIXME: 无法进行点击，有JS跳转
                self.browser.find_element_by_id("J_Static2Quick").click()
                '''
            finally:
                print('正在登录中，请稍后...')
        while "login" in current_url:
            time.sleep(self.__longSleep)
            print('请扫描二维码登录...')
            current_url = self.browser.current_url
        print('登录完成，即将进入购物车...')

    # 全选购物车中所有商品并下单
    def checkout_cart(self, order_time):
        self.browser.get('https://cart.taobao.com/cart.htm')
        while dt.datetime.now() < order_time:
            time.sleep(self.__snapSleep)
        while True:
            try:
                # 全选购物车
                self.browser.find_element_by_id("J_SelectAll2").click()
                time.sleep(self.__shortSleep)
                break
            except:
                time.sleep(self.__snapSleep)
        while True:
            try:
                # 结算
                self.browser.find_element_by_id('J_Go').click()
                time.sleep(self.__shortSleep)
                break
            except:
                time.sleep(self.__snapSleep)
        while self.isTest[0].upper() == 'N': # 提交订单，仅在非测试模式下有效
            try:
                self.browser.find_element_by_link_text("提交订单").click()
                break
            except:
                time.sleep(self.__snapSleep)

    # TODO: 单个商品直接下单
    def checkout_signleItem(self, url, order_time):
        self.browser.get(url)
        while dt.datetime.now() < order_time:
            time.sleep(self.__snapSleep)
        while True:
            if 'tmall' in url:
                try:
                    pass
                except:
                    pass
            elif 'taobao' in url:
                try:
                    pass
                except:
                    pass

if __name__ == "__main__":
    order = TB_order()
    order_time = order.interactive()
    order.webDriver()
    order.login()
    order.checkout_cart(order_time)