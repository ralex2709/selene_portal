from selene import be
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from base_test import BaseTest


class TestAuthorization(BaseTest):
    password = '123456789'
    phone = '(981)437-01-53'


    def test_login(self):
        s('#phone').should(be.blank).click().set_value(self.phone)
        s('#pass').set_value(self.password)
        s('.main-btn_primary').click()
        assert_news_page(

        go_statement()

def assert_news_page():
    s('.thanks-aside').should(be.visible)
    assert browser.driver.current_url == 'https://maxitest.ru/news'

def go_statement(self):
    s('.navigation-link active').click()
    #s('.navigation-sublink').should.(by.be_first_child).click()
    s(by.xpath(".//*[@navigation-sublink='https://maxitest.ru/v2/services/statements/STATEMENT_2NDFL']")).click()
    assert browser.driver.current_url == 'https://maxitest.ru/v2/services/statements/STATEMENT_2NDFL'