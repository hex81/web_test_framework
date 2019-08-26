# -*- coding: utf-8 -*-
# file name: test_web 
# author: hex7
# date: 19/8/2019

from pages.baidu_search import BaiDuSearchPage
from pages.search_result import BaiDuResultPage
from helper.web_search_helper import WebSearchHelper
from basicTest import BasicTest


class TestWebSearch(BasicTest):

    def test_basic_baidu_search(self, test_data):
        # Set up test case data
        phrase = test_data["keyword"]

        search_helper = WebSearchHelper(self.driver)
        result_page = search_helper.get_search_result(phrase)

        # Verify that results appear
        assert result_page.link_div_count() > 0
        assert result_page.phrase_result_count(phrase) > 0
        assert result_page.search_input_value() == phrase

    def test_baidu_search_pic(self):

        keyword = "love.jpg"
        search_helper = WebSearchHelper(self.driver)
        result_page = search_helper.get_search_result(keyword)

        # Verify that results appear
        assert result_page.link_div_count() > 0
        assert result_page.phrase_result_count(keyword) > 0
