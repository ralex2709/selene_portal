from selene import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

browser.open('https://maxitest.ru/login')
s('#phone').should(be.blank).click().set_value('(981)437-01-53')
s('#pass').set_value('123456789')
s('.main-btn_primary').click()
s('.thanks-aside').should(be.visible)
assert browser.driver.current_url == 'https://maxitest.ru/news'

s('.user-arrow').click()
s('.link-logOut').click()
s('#phone').should(be.blank).click().set_value('(981)437-01-53')
s('#pass').set_value('123456789').press_enter()
s('.thanks-aside').should(be.visible)
assert browser.driver.current_url == 'https://maxitest.ru/news'
