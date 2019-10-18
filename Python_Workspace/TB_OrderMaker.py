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

    def __interactive(self):
        print('欢迎使用！当前时间 {}'.format(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        print('程序启动中，请勿关闭此界面...')
        '''
        FIXME:目前大型网站都升级了JS检测，如果识别出使用selenium.webdriver则全部判定为机器人，参考资料提出的解决方法是使用代理绕行
        因此目前输入用户名密码登录功能暂时无法实现
        print('请选择扫描二维码登录或使用用户名密码登录...')
        login_method = input('扫描二维码登录请输入0，使用密码登录请输入1（默认使用二维码登录）：')
        if login_method == '1':
            userName = input('请输入用户名：')
            userPassword = getpass.getpass('请输入密码：')
            time.sleep(__shortSleep)
            print('目前无法使用用户名密码登录')
        else:
            print('请准备扫描二维码...')
            time.sleep(__longSleep)
        '''
        self.__isTest = input('请确认是否进入测试模式(Y/N)...')
        if self.__isTest[0].upper() == 'N':
            self.__order_time = input('请输入目标下单时间，格式为 YYYY-MM-DD HH:MM:SS：')
            self.__order_time = dt.datetime.strptime(self.__order_time, '%Y-%m-%d %H:%M:%S')
        else:
            print('测试模式启动，不会确认订单...')
        self.__isSingle = input('请确认购买单件商品（Y）或全选购物车商品（N）：')
        while self.__isSingle.upper() != 'Y' and self.__isSingle.upper() != 'N':
            self.__isSingle = input('请确认购买单件商品（Y）或全选购物车商品（N）：')
        if self.__isSingle.upper() == 'Y':
            self.url = input('请填入商品的网址...')
            if self.__isTest[0].upper() == 'Y':
                self.__order_time = dt.datetime.now() + dt.timedelta(minutes = 1)
        print('下单时间为：{}'.format(self.__order_time))

    # 启动webdriver
    def __webDriver(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()

    def __login(self, usePassword = '0', userName = 'userName', userPassword = 'userPassword'):
        self.browser.get('https://www.taobao.com')
        time.sleep(self.__enoughSleep)

        self.browser.find_element_by_link_text("亲，请登录").click()
        time.sleep(self.__longSleep)
        current_url = self.browser.current_url

        if usePassword == '1':
            try:
                self.browser.find_element_by_css_selector(".login-box.no-longlogin.module-static")
            except:
                self.browser.find_element_by_css_selector(".login-box.no-longlogin.module-quick")
                self.browser.find_element_by_id("J_Quick2Static").click()
            inputUser = self.browser.find_element_by_id("TPL_username_1")
            inputUser.clear()
            inputUser.send_keys(userName)
            time.sleep(self.__longSleep)
            inputPassword = self.browser.find_element_by_id("TPL_password_1")
            inputPassword.clear()
            inputPassword.send_keys(userPassword)
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
        print('登录完成...')

    # 全选购物车中所有商品并下单
    def __checkoutCart(self):
        self.browser.get('https://cart.taobao.com/cart.htm')
        while dt.datetime.now() < self.__order_time:
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

    def __checkoutSignleItem(self):
        self.browser.get(self.url)
        while dt.datetime.now() < self.__order_time:
            time.sleep(self.__snapSleep)
        while True:
            try:
                self.browser.find_element_by_link_text("立即购买").click()
                break
            except:
                time.sleep(self.__snapSleep)

    def makeOrder(self):
        self.__interactive()
        self.__webDriver()
        self.__login()
        if self.__isSingle.upper() == 'Y':
            self.__checkoutSignleItem()
        else:
            self.__checkoutCart()
        while self.__isTest[0].upper() == 'N': # 提交订单，仅在非测试模式下有效
            try:
                self.browser.find_element_by_link_text("提交订单").click()
                break
            except:
                time.sleep(self.__snapSleep)


if __name__ == "__main__":
    order = TB_order()
    order.makeOrder()