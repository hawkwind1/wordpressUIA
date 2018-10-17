#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 22:25
# @Author  : PanCheng
# @Site    : 
# @File    : dashboardpage.py
# @Software: PyCharm
from pages.basepage import BasePage
from pages.topiclistpage import TopicListPage


class DashBoardPage(BasePage):

    # init
    def __init__(self, driver, path="wp-admin/index.php"):
        super(DashBoardPage, self).__init__(driver, path)

    # get elements
    @property
    def _topic_menu_on_browser(self):
        return self._by_css("#menu-posts > a > div.wp-menu-name")

    # public actions
    @property
    def greeting_link(self):
        return self._by_css("#wp-admin-bar-my-account .ab-item")

    def navigate_to_topic_list_page(self):
        self._topic_menu_on_browser.click()
        return TopicListPage(self.driver)

