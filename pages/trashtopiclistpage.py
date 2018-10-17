#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 22:30
# @Author  : PanCheng
# @Site    : 
# @File    : trashtopiclistpage.py
# @Software: PyCharm

from pages.basepage import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class TrashTopicListPage(BasePage):

    # 初始化页面
    def __init__(self, driver, path="wp-admin/edit.php?post_status=trash&post_type=post"):
        super(TrashTopicListPage, self).__init__(driver, path)

    def _topic_item(self, post_id):
        """
        根据post_id,在文章列表中查找的文章条目element
        :param post_id:
        :return:
        """
        css_string = "#post-{} > td.title.column-title." \
                     "has-row-actions.column-primary." \
                     "page-title".format(post_id)
        return self._by_css(css_string)

    def _del_a_topic_item_thoroughly_menu(self, post_id):
        """
        移动鼠标到文章列表中给定post_id的文章条目,展现"永久删除"菜单
        :param post_id:
        :return:
        """
        css_string1 = "#post-{} > td.title.column-title.has-" \
                      "row-actions.column-primary.page-" \
                      "title".format(post_id)
        topic_item_element = self._by_css(css_string1)
        actions = ActionChains(self.driver)
        actions.move_to_element(topic_item_element)
        actions.perform()

        css_string2 = "#post-{} > td.title.column-title." \
                      "has-row-actions.column-primary.page" \
                      "-title > div.row-actions > span" \
                      ".delete > a".format(post_id)
        return self._by_css(css_string2)

    def del_a_topic_item_throguly_by_post_id(self, post_id):
        """
        将给定post_id的文章彻底删除
        :param post_id:
        :return:
        """
        self._del_a_topic_item_thoroughly_menu(post_id).click()