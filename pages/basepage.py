#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 22:25
# @Author  : PanCheng
# @Site    :
# @File    : basepage.py
# @Software: PyCharm
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

TIMEOUT = 10
DOMAIN = "http://139.199.192.100:8000/"


class BasePage(object):

    # 所有页面的初始化方法, 一是driver; 二是 base_url
    def __init__(self, driver, path=None):
        self.driver = driver

        if path:
            self.url = DOMAIN + path
        else:
            self.url = None

        # 如果传入的self.url不为空,而且与当前页面url不一致,跳转到self.url
        # 有些页面的链接点击后,会自动跳转到新页面,这种清空下,就不需重新
        if self.url is not None and (self.driver.current_url != self.url):
            self._navigate()

    # 用浏览器打开网页
    def _navigate(self):
        self.driver.get(self.url)

    # 封装获取网页title的方法,方便外部直接用page对象调用获取title信息
    def get_title(self):
        return self.driver.get_title()

    # 封装获取网页url的方法,方便外部直接用page对象调用获取url信息
    def get_url(self):
        return self.driver.current_url

    # 封装部分find elements的方法,方便子pages使用
    def _by_css(self, css_string):
        element = WebDriverWait(self.driver,TIMEOUT).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_string)))
        return element

    def _check_element_not_exist_by_css(self, css_string):
        return EC.invisibility_of_element_located((By.CSS_SELECTOR, css_string))

    def _by_id(self, id_string):
        return self.driver.find_element_by_id(id_string)

    # def xxx(self):
    #     pass