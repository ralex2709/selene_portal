import time

from selene import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from kernel.local_storage import LocalStorage


class BaseTest:
    password = '123456789'
    phone = '(981)437-01-53'

    def setup(self):
        self.config()
        self.login()

    def teardown(self):
        self.logout()

    def config(self):
        browser.open('https://maxitest.ru/login')
        browser.config.browser_name = 'chrome'
        browser.config.reports_folder = './screens'
        local_storage = LocalStorage(browser.driver)
        local_storage.set('push', str(int(round(time.time() * 1000))))

    def login(self):
        s('#phone').should(be.blank).click().set_value(self.phone)
        s('#pass').set_value(self.password)
        s('.main-btn_primary').click()
        self.assert_news_page()

    def logout(self):
        s('.user-arrow').click()
        s('.link-logOut').click()

    def assert_news_page(self):
        s('.thanks-aside').should(be.visible)
        assert browser.driver.current_url == 'https://maxitest.ru/news'

