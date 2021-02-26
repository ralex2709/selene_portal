from selene import be
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

password = '123456789'
phone = '(981)437-01-53'


def login_test(browser_name):
    browser.open('https://maxitest.ru/login')
    browser.config.browser_name = browser_name
    browser.config.reports_folder = './screens'
    s('#phone').should(be.blank).click().set_value(phone)
    s('#pass').set_value(password)
    s('.main-btn_primary').click()
    assert_news_page()

    logout()
    s('#phone').should(be.blank).click().set_value(phone)
    s('#pass').set_value(password).press_enter()
    assert_news_page()

    logout()
    go_captcha()
    back()

    go_captcha()
    set_captcha()

    back()
    go_captcha()
    set_captcha()

    back()
    go_captcha()
    set_captcha()
    set_sms()

    back()
    go_captcha()
    set_captcha()
    set_sms()
    s('#pass').set_value(password)
    s('#passConfirm').set_value(password)
    s('.main-btn_primary').click()

    assert_news_page()


def assert_news_page():
    s('.thanks-aside').should(be.visible)
    assert browser.driver.current_url == 'https://maxitest.ru/news'


def logout():
    s('.user-arrow').click()
    s('.link-logOut').click()


def back():
    s(by.link_text('Вернуться')).click()
    s('#pass').should(be.visible)
    assert browser.driver.current_url == 'https://maxitest.ru/login'


def go_captcha():
    s(by.link_text('Восстановление пароля')).click()
    s('#captcha').should(be.blank)
    assert browser.driver.current_url == 'https://maxitest.ru/recover'


def set_captcha():
    s('#phone').should(be.blank).click().set_value(phone)
    s('#captcha').set_value('йцукен')
    s('.main-btn_primary').click()


def set_sms():
    s('#confirmationCode').set_value('12345')
    s('.main-btn_primary').click()


# login_test('firefox')
login_test('chrome')
