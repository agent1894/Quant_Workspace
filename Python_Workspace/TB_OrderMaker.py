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

def login(use_password = 0):
    browser.get('https://www.taobao.com')
    time.sleep(enoughSleep)

    browser.find_element_by_link_text("亲，请登录").click()
    time.sleep(longSleep)
    current_url = browser.current_url
    '''
    TODO:
    1. 进入登录界面后，无法对扫描二维码和输入用户名密码做切换，报错：Element is not clickable at point
    2. 在输入用户名和密码后无法通过滑动验证码检验
    '''
    # if use_password == '1':
    #     browser.find_element_by_link_text("密码登录").click()
    #     time.sleep(longSleep)
    #     input_user = browser.find_element_by_id("TPL_username_1")
    #     input_user.send_keys(user_name)
    #     time.sleep(longSleep)
    #     input_password = browser.find_element_by_id("TPL_password_1")
    #     input_password.send_keys(user_password)
    #     time.sleep(longSleep)
    #     browser.find_element_by_id("J_SubmitStatic").click()
    # else:
    #     try:
    #         browser.find_element_by_id("J_Quick2Static").click()
    #     except:
    #         browser.find_element_by_id("J_Static2Quick").click()
    #     finally:
    #         print('Waiting for scanning the QR code...')
    while "login" in current_url:
        time.sleep(longSleep)
        print('Waiting for scanning the QR code or enter the password...')
        current_url = browser.current_url
    print('Ready for getting cart...')

def checkout(order_time=dt.datetime.now()):
    browser.get('https://cart.taobao.com/cart.htm')
    while dt.datetime.now() < order_time:
        time.sleep(snapSleep)
    while True:
        try:
            browser.find_element_by_id("J_SelectAll2").click()
            time.sleep(shortSleep)
            break
        except:
            time.sleep(snapSleep)
    while True:
        try:
            browser.find_element_by_id('J_Go').click()
            time.sleep(shortSleep)
            break
        except:
            time.sleep(snapSleep)
    while True:
        try:
            browser.find_element_by_link_text("提交订单").click()
            break
        except:
            time.sleep(snapSleep)

if __name__ == "__main__":
    date_time = dt.datetime.now()
    snapSleep = 0.01
    shortSleep = 0.1
    longSleep = 1
    enoughSleep = 3
    print('欢迎使用！当前时间 {}'.format(date_time.strftime('%Y-%m-%d %H:%M:%S')))
    print('程序启动中，请勿关闭此界面...')
    order_time = input('请输入目标时间，格式为 YYYY-MM-DD HH:MM:SS：')
    order_time = dt.datetime.strptime(order_time, '%Y-%m-%d %H:%M:%S')
    print('请选择扫描二维码登录或使用用户名密码登录...')
    login_method = input('扫描二维码登录请输入0，使用密码登录请输入1（默认使用二维码登录）：')
    if login_method == '1':
        user_name = input('请输入用户名：')
        user_password = getpass.getpass('请输入密码：')
        time.sleep(shortSleep)
    elif login_method == '1':
        print('请准备扫描二维码...')
        time.sleep(longSleep)
    
    browser = webdriver.Chrome()
    browser.maximize_window()
    login(login_method)
    checkout(order_time)