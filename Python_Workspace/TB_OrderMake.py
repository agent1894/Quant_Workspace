#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Taobao 
from selenium import webdriver
import selenium
import datetime as dt
import time
import os

date_time = dt.datetime.now()
print('Welcome! Now is {}'.format(date_time.strftime('%Y-%m-%d %H:%M:%S')))
print('Program starts...')

def login():
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    time.sleep(3)
    try:
    # if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        # print(browser.current_url)
        # time.sleep(15)
        # browser.get('https://cart.taobao.com/cart.htm')
        # if browser.find_element_by_id("J_SelectAll2"):
        #     browser.find_element_by_id("J_SelectAll2").click()
        #     time.sleep(1)
        # if browser.find_element_by_link_text("结 算"):
        #     browser.find_element_by_link_text("结 算").click()
        #     time.sleep(1)
        # if browser.find_element_by_link_text("提交订单"):
        #     browser.find_element_by_link_text("提交订单").click()
    except selenium.common.exceptions.NoSuchElementException:

login()