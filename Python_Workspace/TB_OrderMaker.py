#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import selenium
import datetime as dt
import time
import getpass

def login(use_password = 0):
    browser.get('https://www.taobao.com')
    time.sleep(3)

    browser.find_element_by_link_text("亲，请登录").click()
    time.sleep(1)
    current_url = browser.current_url
    if use_password == '1': #FIXME: can not automatic login, waiting for fix
        browser.find_element_by_link_text("密码登录").click()
        time.sleep(1)
        input_user = browser.find_element_by_id("TPL_username_1")
        input_user.send_keys(user_name)
        time.sleep(1)
        input_password = browser.find_element_by_id("TPL_password_1")
        input_password.send_keys(user_password)
        time.sleep(1)
        browser.find_element_by_id("J_SubmitStatic").click()
    else:
        if browser.find_element_by_link_text("密码登录"):
            print('Waiting for scanning the QR code...')
        else:
            browser.find_element_by_id("J_LoginBox").click()
    while "login" in current_url:
        time.sleep(0.5)
        print('Waiting for scanning the QR code or enter the password...')
        current_url = browser.current_url
    print('Ready for getting cart...')

def checkout(order_time=dt.datetime.now()):
    browser.get('https://cart.taobao.com/cart.htm')
    while dt.datetime.now() < order_time and browser.find_element_by_id("J_SelectAll2"):
        time.sleep(0.001)
    browser.find_element_by_id("J_SelectAll2").click()
    # time.sleep(1)
    while not browser.find_element_by_class_name("submit-btn"):
        time.sleep(0.001)
    browser.find_element_by_link_text("结 算").click()
    # while not browser.find_element_by_link_text("提交订单"):
    #     time.sleep(0.001)
    # browser.find_element_by_link_text("提交订单").click()

if __name__ == "__main__":
    date_time = dt.datetime.now()
    print('Welcome! Now is {}'.format(date_time.strftime('%Y-%m-%d %H:%M:%S')))
    print('Program starts...')
    print('Do you want to login by scanning the QR code or entering the password?')
    login_method = input('If you want to use QR code please enter 0, else enter 1: ')
    if login_method == '0':
        print('Please prepare the telephone and wait for scanning...')
    else:
        user_name = input('Please enter the username: ')
        user_password = getpass.getpass('Please enter the password: ')
    order_time = input('Please enter your target ordering time: (use format: YYYY-MM-DD HH:MM:SS)')
    order_time = dt.datetime.strptime(order_time, '%Y-%m-%d %H:%M:%S')
    
    browser = webdriver.Chrome()
    browser.maximize_window()
    login(login_method)
    checkout(order_time)