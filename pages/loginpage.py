#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 22:25
# @Author  : PanCheng
# @Site    : 
# @File    : loginpage.py
# @Software: PyCharm
from pages.basepage import BasePage
from pages.dashboardpage import DashBoardPage
import time


class LoginPage(BasePage):

    def __init__(self, driver, path="wp-login.php"):
        super(LoginPage, self).__init__(driver, path)

    @property
    def _usename_text_field(self):
        return self._by_css("#user_login")

    @property
    def _password_text_field(self):
        return self._by_css("#user_pass")

    @property
    def _login_button(self):
        return self._by_css("#wp-submit")

    def login(self, username, password):
        time.sleep(1)
        self._usename_text_field.clear()
        self._password_text_field.clear()
        self._usename_text_field.send_keys(username)
        self._password_text_field.send_keys(password)
        self._login_button.click()

        return DashBoardPage(self.driver)

    def login_as_pyse17(self):
        """
        用于正常登录系统
        :return:
        """
        return self.login("pyse17", "pyse17")

    def login_as_expecting_error(self, username, password):
        time.sleep(1)
        self._usename_text_field.clear()
        self._password_text_field.clear()
        self._usename_text_field.send_keys(username)
        self._password_text_field.send_keys(password)
        self._login_button.click()

        error_message = self._by_css("#login_error").text
        return error_message

