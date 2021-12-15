from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from selene import be
from selene import command

from base_test import BaseTest


class TestBusinessCard(BaseTest):
    fio_portal = 'Тестовый тест'
    fio_not_portal = 'Токач Диана'

    def setup(self):
        super().setup()
        s('#test-services_nav').hover()
        s('#test-services_nav__businessCards').click()

    def test_simple(self):
        s('#test-services_business-card__button').click()
        s('.business-card-modal__body').should(be.visible)
        s('.close-modal').click()

    def test_fio(self):
        browser.driver.execute_script("window.scrollTo(0, 0)")
        s('#test-services_business-card__fio').should(be.visible)
        s('#test-services_business-card__fio').click()
        s('#test-services_business-card__fio').clear()
        s('#test-services_business-card__fio').click().set_value(self.fio_portal)
        ss('.user-finder-option__name').element(1).click()
        #browser.driver.execute_script('#test-services_business-card__button')
        s('#test-services_business-card__button').should(be.visible)
        s('#test-services_business-card__button').click()
        s('.close-modal').click()
