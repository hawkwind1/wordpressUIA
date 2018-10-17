#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 22:26
# @Author  : PanCheng
# @Site    : 
# @File    : topiclistpage.py
# @Software: PyCharm
from pages.basepage import BasePage
from pages.newtopicpage import NewTopicPage
from selenium.webdriver.common.action_chains import ActionChains


class TopicListPage(BasePage):

    def __init__(self, driver, path="wp-admin/edit.php"):
        super(TopicListPage, self).__init__(driver, path)

    # find elements
    @property
    def _write_topic_menu(self):
        return self._by_css("#wpbody-content > div.wrap > a")

    def _topic_item(self, post_id):
        """
        :param post_id:
        :return: 根据post_id,在文章列表中查找的文章条目element
        """
        css = "#post-{} > td.title.column-title.has-row-actions" \
              ".column-primary.page-title > strong > a".format(post_id)
        return self._by_css(css)

    def _check_topic_item_not_exist(self, post_id):
        """
        :param post_id:
        :return: 根据post_id,在文章列表中查找的文章条目是否存在,不存在返回True
        """
        css = "#post-{} > td.title.column-title.has-row-actions" \
              ".column-primary.page-title > strong > a".format(post_id)
        return self._check_element_not_exist_by_css(css)

    # private actions
    def _move_item_to_trash_bin_menu(self, post_id):
        """

        :param post_id:
        :return: 移动到文章psot_id对应的标题,展现的"移至回收站"element
        """
        topic_item = self._topic_item(post_id)
        actions = ActionChains(self.driver)
        actions.move_to_element(topic_item)
        actions.perform()

        css2 = "#post-{} > td.title.column-title.has-row" \
              "-actions.column-primary.page-title >" \
              " div.row-actions > span.trash > a".format(post_id)
        return self._by_css(css2)

    # public actions
    def topic_item_not_exist(self, post_id):
        return self._check_topic_item_not_exist(post_id)

    def move_topic_to_trash_bin_by_post_id(self, post_id):
        """
        将给定post_id的文章移动到回收站
        :param post_id:
        :return:
        """
        self._move_item_to_trash_bin_menu(post_id).click()

    def navigate_to_write_topic_page(self):
        self._write_topic_menu.click()
        return NewTopicPage(self.driver)

    def get_topic_text_by_post_id(self, post_id):
        return self._topic_item(post_id).text


