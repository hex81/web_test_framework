# -*- coding: utf-8 -*-
# file name: web_search_helper 
# author: hex7
# date: 19/8/2019

from pages.baidu_search import BaiDuSearchPage
from pages.search_result import BaiDuResultPage


class WebSearchHelper:

    def __init__(self, browser):
        self.search_page = BaiDuSearchPage(browser)
        self.result = BaiDuResultPage(browser)

    def get_search_result(self, phase):
        self.search_page.load()
        self.search_page.search(phase)

        return self.result
