from time import sleep

from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from selene import be, have

from base_test import BaseTest


class TestBusinessCard(BaseTest):
    password = '123456789'
    phone = '(981)437-01-53'


    def setup(self):
        super().setup()
        s('#test-services_nav').hover()
        s('#test-services_nav__businessCards').click()
        assert browser.driver.current_url == 'https://maxitest.ru/services/business-card'

    def test_simple(self):
        s('#test-services_business-card__button').click()
        # sleep(1)
        s('.business-card-modal__body').should(be.visible)
        s('.close-modal').click()
