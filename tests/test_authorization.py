from selene import be
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from base_test import BaseTest


class TestAuthorization(BaseTest):
    password = '123456789'
    phone = '(981)437-01-53'

    def setup(self):
        self.config()

    def test_login(self):
        s('#phone').should(be.blank).click().set_value(self.phone)
        s('#pass').set_value(self.password)
        s('.main-btn_primary').click()
        assert_news_page()

        self.logout()
        s('#phone').should(be.blank).click().set_value(self.phone)
        s('#pass').set_value(self.password).press_enter()
        assert_news_page()

        self.logout()
        go_captcha()
        back()

        go_captcha()
        self.set_captcha()

        back()
        go_captcha()
        self.set_captcha()

        back()
        go_captcha()
        self.set_captcha()
        set_sms()

        back()
        go_captcha()
        self.set_captcha()
        set_sms()
        s('#pass').set_value(self.password)
        s('#passConfirm').set_value(self.password)
        s('.main-btn_primary').click()

        assert_news_page()

    def set_captcha(self):
        s('#phone').should(be.blank).click().set_value(self.phone)
        s('#captcha').set_value('йцукен')
        s('.main-btn_primary').click()


def assert_news_page():
    s('.thanks-aside').should(be.visible)
    assert browser.driver.current_url == 'https://maxitest.ru/news'


def back():
    s(by.link_text('Вернуться')).click()
    s('#pass').should(be.visible)
    assert browser.driver.current_url == 'https://maxitest.ru/login'


def go_captcha():
    s(by.link_text('Восстановление пароля')).click()
    s('#captcha').should(be.blank)
    assert browser.driver.current_url == 'https://maxitest.ru/recover'


def set_sms():
    s('#confirmationCode').set_value('12345')
    s('.main-btn_primary').click()
