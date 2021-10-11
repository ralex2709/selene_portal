from selene import be
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

from base_test import BaseTest


class TestStatments(BaseTest):
    password = '123456789'
    phone = '(981)437-01-53'


    def test_login(self):
        go_statement()

def assert_news_page():
    s('.thanks-aside').should(be.visible)
    assert browser.driver.current_url == 'https://maxitest.ru/news'

def go_statement():
    s('#test-services_nav').click()
    s('#test-services_nav__statements').click()
    assert browser.driver.current_url == 'https://maxitest.ru/v2/services/statements/STATEMENT_2NDFL'
    ss('.input-base-control').element(1).click().set_value('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    s('.main-btn_primary').click()
    s('.modal__wrapper').should(be.visible)
    s('.modal__close').click()
    ss('.services-aside__link').element(1).click()
    assert browser.driver.current_url == 'https://maxitest.ru/v2/services/statements/STATEMENT_INCOME'
    ss('.input-base-control').element(1).click().set_value('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    s('.main-btn_primary').click()
    s('.modal__wrapper').should(be.visible)
    s('.modal__close').click()
    ss('.services-aside__link').element(2).click()
    assert browser.driver.current_url == 'https://maxitest.ru/v2/services/statements/STATEMENT_182H'
    ss('.input-base-control').element(1).click().set_value('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    s('.main-btn_primary').click()
    s('.modal__wrapper').should(be.visible)
    s('.modal__close').click()
    ss('.services-aside__link').element(3).click()
    assert browser.driver.current_url == 'https://maxitest.ru/v2/services/statements/STATEMENT_VISA'
    # ss('.input-base-control').element(1).click().set_value('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    # s('.main-btn_primary').click()
    # s('.modal__wrapper').should(be.visible)
    # s('.modal__close').click()
    ss('.services-aside__link').element(4).click()
    assert browser.driver.current_url == 'https://maxitest.ru/v2/services/statements/STATEMENT_OTHER'
    s('.input-base-control').click().set_value('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    s('.main-btn_primary').click()
    s('.modal__wrapper').should(be.visible)
    s('.modal__close').click()
    ss('.services-aside__link').element(5).click()
    assert browser.driver.current_url == 'https://maxitest.ru/v2/services/statements/STATEMENT_EMPLOYMENT_HISTORY'
    s('.input-base-control').click().set_value('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    s('.main-btn_primary').click()
    s('.modal__wrapper').should(be.visible)
    s('.modal__close').click()



