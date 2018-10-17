#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 22:31
# @Author  : PanCheng
# @Site    : 
# @File    : newtopicpage.py
# @Software: PyCharm
from pages.basepage import BasePage


class NewTopicPage(BasePage):

    def __init__(self, driver, path="wp-admin/post-new.php"):
        super(NewTopicPage, self).__init__(driver, path)

    @property
    def _title_input_box(self):
        return self._by_css("#title")

    def _switch_2_frame(self):
        self.driver.switch_to.frame("content_ifr")

    def _switch_2_default(self):
        self.driver.switch_to.default_content()

    @property
    def _content_input_box(self):
        return self._by_css("#tinymce")

    @property
    def _push_button(self):
        return self._by_css("#publish")

    @property
    def _post_id(self):
        # return self._by_css("#post_ID").get_attribute("value")
        # 注意这里的元素在页面上不可见,而封装的_by_css使用了visibility_of_element_located,所以一定会报错
        return self._by_id("post_ID").get_attribute("value")

    def write_and_push_a_new_topic(self, topic_title, topic_content):
        """

        :return: post_ID for the new topic
        """
        # 提取post_id
        post_id = self._post_id

        self._title_input_box.send_keys(topic_title)
        self._switch_2_frame()
        self._content_input_box.send_keys(topic_content)
        self._switch_2_default()
        self._push_button.click()

        return post_id

