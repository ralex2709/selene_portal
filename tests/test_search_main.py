from selene import be, by, query
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

from base_test import BaseTest


class TestSearchMain(BaseTest):
    batrakova_url = 'https://maxitest.ru/user/5978'

    def test_search_contacts(self):
        self.search_input('батракова')
        self.assert_batrakova_color('Батракова')
        ss('.info-name').element(0).click()
        self.assert_batrakova_url()

        self.search_input(',fnhfrjdf')
        ss(by.text('Батракова Александра Эдуардовна')).element(0).click()
        self.assert_batrakova_url()

        self.search_input('александра батракова')
        self.assert_batrakova_color('Александра')
        ss('.info-name').element(0).click()
        self.assert_batrakova_url()

        self.search_input('але')
        ss('.search-view .block-resultLink').element(0).click()
        assert browser.driver.current_url == 'https://maxitest.ru/search/CONTACT/%D0%B0%D0%BB%D0%B5'

    def search_input(self, text):
        s('#search-input').should(be.visible).set_value(text)

    def assert_batrakova_color(self, text):
        assert ss('.info-name .search-color').element(0).get(query.text) == text

    def assert_batrakova_url(self):
        assert browser.driver.current_url == self.batrakova_url
        s('.header-logo').click()
        s('.maxiportalQR-btn').should(be.visible)
