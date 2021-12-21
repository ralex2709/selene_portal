from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from selene import be
from selene import command

from base_test import BaseTest


class TestBusinessCard(BaseTest):
    fio_portal = 'Тестовый тест'
    fio_not_portal = 'Токач Диана'
    position_valid = 'Тестовая позиция'
    tel_valid = '782086(вн.1817)'
    address_valid = 'Вологда, Ярославская 32, каб 155'
    mail_valid = 'test@test.ru'
    fio_eng_valid = 'Testovy test'
    position_eng_valid = 'testovaya pozitciya'
    tel_eng_valid = '782086(vn.1817)'
    address_eng_valid = 'Vologda, Yaroslavskaya 32, office 155'
    comment_valid = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    comment_invalid = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo1'
    fio_eng_invalid = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, co'
    position_eng_invalid = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, co'
    tel_eng_invalid = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, co'
    address_eng_invalid = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, co'
    mail_invalid = 'ekjekrjgkdfgdfklgdfklgj'
    def setup(self):
        super().setup()
        s('#test-services_nav').hover()
        s('#test-services_nav__businessCards').click()

    def test_simple(self):
        s('#test-services_business-card__button').click()
        s('.business-card-modal__body').should(be.visible)
        s('.close-modal').click()

    def test_fio(self):
        #browser.driver.execute_script("window.scrollTo(0, 0)")
        s('#test-services_business-card__fio').should(be.visible)
        s('#test-services_business-card__fio').click()
        s('#test-services_business-card__fio').clear()
        s('#test-services_business-card__fio').click().set_value(self.fio_portal)
        ss('.user-finder-option__name').element(1).click()
        #browser.driver.execute_script('#test-services_business-card__button')
        #browser.driver.execute_script("window.scrollTo(0, 0)")
        s('#test-services_business-card__button').should(be.visible)
        browser.driver.execute_script("window.scrollTo(1000, 0)")
        s('#test-services_business-card__button').click()
        s('.close-modal').click()

    def test_1(self): # все поля заполнены корректно
        s('#test-services_business-card__fio').should(be.visible)
        s('#test-services_business-card__position').click()
        s('#test-services_business-card__position').clear()
        s('#test-services_business-card__position').click().set_value(self.position_valid)
        s('#test-services_business-card__phone').click()
        s('#test-services_business-card__phone').clear()
        s('#test-services_business-card__phone').click().set_value(self.tel_valid)
        s('#test-services_business-card__address').click()
        s('#test-services_business-card__address').clear()
        s('#test-services_business-card__address').click().set_value(self.address_valid)
        s('#test-services_business-card__email').click()
        s('#test-services_business-card__email').clear()
        s('#test-services_business-card__email').click().set_value(self.mail_valid)
        s('#test-services_business-card__quantity50').click()
        #browser.driver.execute_script("window.scrollTo('#test-services_business-card__button')")
        s('.edit-switch__slider').click()
        s('#test-services_business-card__fioEN').click().set_value(self.fio_eng_valid)
        s('#test-services_business-card__positionEN').click().set_value(self.position_eng_valid)
        s('#test-services_business-card__phone2').click().set_value(self.tel_eng_valid)
        s('#test-services_business-card__addressEN').click().set_value(self.address_eng_valid)
        s('#test-services_business-card__email2').click().set_value(self.mail_valid)
        s('#test-services_business-card__comment').click().set_value(self.comment_valid)
        s('#test-services_business-card__button').click()
        s('.close-modal').click()

    def test_2(self): # проверка ошибки ввода в поле почта для англ
        s('#test-services_business-card__fio').should(be.visible)
        s('#test-services_business-card__position').click()
        s('#test-services_business-card__position').clear()
        s('#test-services_business-card__position').click().set_value(self.position_valid)
        s('#test-services_business-card__phone').click()
        s('#test-services_business-card__phone').clear()
        s('#test-services_business-card__phone').click().set_value(self.tel_valid)
        s('#test-services_business-card__address').click()
        s('#test-services_business-card__address').clear()
        s('#test-services_business-card__address').click().set_value(self.address_valid)
        s('#test-services_business-card__email').click()
        s('#test-services_business-card__email').clear()
        s('#test-services_business-card__email').click().set_value(self.mail_valid)
        s('#test-services_business-card__quantity150').click()
        s('.edit-switch__slider').click()
        s('#test-services_business-card__fioEN').click().set_value(self.fio_eng_invalid)
        s('#test-services_business-card__positionEN').click().set_value(self.position_eng_invalid)
        s('#test-services_business-card__phone2').click().set_value(self.tel_eng_invalid)
        s('#test-services_business-card__addressEN').click().set_value(self.address_eng_invalid)
        s('#test-services_business-card__email2').click().set_value(self.mail_invalid)
        s('#test-services_business-card__comment').click().set_value(self.comment_invalid)
        s('#test-services_business-card__button').click()
        s('.input-base-control_error').should(be.visible)
        s('#test-services_business-card__email2').click().clear().set_value(self.mail_valid)
        s('#test-services_business-card__button').click()
        s('.close-modal').click()

    def test_3(self): #test №1 из файла "тестирование сервисов"
        s('#test-services_business-card__fio').should(be.visible)
        s('#test-services_business-card__position').click()
        s('#test-services_business-card__position').clear()
        s('#test-services_business-card__position').click().set_value(self.position_valid)
        s('#test-services_business-card__phone').click()
        s('#test-services_business-card__phone').clear()
        s('#test-services_business-card__phone').click().set_value(self.tel_valid)
        s('#test-services_business-card__address').click()
        s('#test-services_business-card__address').clear()
        s('#test-services_business-card__address').click().set_value(self.address_valid)
        s('#test-services_business-card__email').click()
        s('#test-services_business-card__email').clear()
        s('#test-services_business-card__email').click().set_value(self.mail_valid)
        s('#test-services_business-card__quantity150').click()
        s('.edit-switch__slider').click()
        s('#test-services_business-card__fioEN').click().set_value(self.fio_eng_invalid)
        s('#test-services_business-card__positionEN').click().clear()
        s('#test-services_business-card__phone2').click().set_value(self.tel_eng_valid)
        s('#test-services_business-card__addressEN').click().set_value(self.address_eng_invalid)
        s('#test-services_business-card__email2').click().set_value(self.mail_valid)
        s('#test-services_business-card__comment').click().set_value(self.comment_invalid)
        s('#test-services_business-card__button').click()
        s('.input-base-control_error').should(be.visible)
        s('#test-services_business-card__positionEN').click().set_value(self.position_eng_valid)
        s('#test-services_business-card__button').click()
        s('.close-modal').click()

    def test_4(self): # тест №2 из файла "Тестирование сервисов"
        s('#test-services_business-card__fio').should(be.visible)
        s('#test-services_business-card__position').should(be.visible)
        s('#test-services_business-card__phone').should(be.visible)
        s('#test-services_business-card__address').should(be.visible)
        s('#test-services_business-card__email').should(be.visible)
        s('#test-services_business-card__quantity100').click()
        s('.edit-switch__slider').click()
        s('#test-services_business-card__fioEN').click().set_value(self.fio_eng_invalid)
        s('#test-services_business-card__positionEN').click().clear()
        s('#test-services_business-card__positionEN').click().set_value(self.position_eng_invalid)
        s('#test-services_business-card__phone2').should(be.visible)
        s('#test-services_business-card__addressEN').click().set_value(self.address_eng_valid)
        s('#test-services_business-card__comment').should(be.visible)
        s('#test-services_business-card__button').click()
        s('.close-modal').click()

    def test_5(self): # тест №3 из файла "Тестирование сервисов"
        s('#test-services_business-card__fio').should(be.visible)
        s('#test-services_business-card__position').click()
        s('#test-services_business-card__position').clear()
        s('#test-services_business-card__position').click().set_value(self.position_valid)
        s('#test-services_business-card__phone').click()
        s('#test-services_business-card__phone').clear()
        s('#test-services_business-card__phone').click().set_value(self.tel_valid)
        s('#test-services_business-card__address').click()
        s('#test-services_business-card__address').clear()
        s('#test-services_business-card__address').click().set_value(self.address_valid)
        s('#test-services_business-card__email').click()
        s('#test-services_business-card__email').clear()
        s('#test-services_business-card__email').click().set_value(self.mail_valid)
        s('#test-services_business-card__quantity50').click()
        s('.edit-switch__slider').click()
        s('#test-services_business-card__fioEN').should(be.visible)
        s('#test-services_business-card__positionEN').click().set_value(self.position_eng_valid)
        s('#test-services_business-card__phone2').click().set_value(self.tel_eng_valid)
        s('#test-services_business-card__addressEN').should(be.visible)
        s('#test-services_business-card__email2').click().set_value(self.mail_valid)
        s('#test-services_business-card__comment').click().set_value(self.comment_valid)
        s('#test-services_business-card__button').click()
        s('.input-base_error').should(be.visible)
        s('#test-services_business-card__fioEN').click().set_value(self.fio_eng_valid)
        s('#test-services_business-card__addressEN').click().set_value(self.address_eng_valid)
        s('#test-services_business-card__button').click()
        s('.close-modal').click()

    def test_6(self): # тест №4 из файла "Тестирование сервисов"
        s('#test-services_business-card__fio').should(be.visible)
        s('#test-services_business-card__position').click()
        s('#test-services_business-card__position').clear()
        s('#test-services_business-card__position').click().set_value(self.position_valid)
        s('#test-services_business-card__phone').click()
        s('#test-services_business-card__phone').clear()
        s('#test-services_business-card__phone').click().set_value(self.tel_valid)
        s('#test-services_business-card__address').click()
        s('#test-services_business-card__address').clear()
        s('#test-services_business-card__address').click().set_value(self.address_valid)
        s('#test-services_business-card__email').click()
        s('#test-services_business-card__email').clear()
        s('#test-services_business-card__email').click().set_value(self.mail_valid)
        s('#test-services_business-card__quantity50').click()
        s('.edit-switch__slider').click()