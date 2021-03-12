from selene import be, have, by
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss, s

from base_test import BaseTest


class TestHistory(BaseTest):

    #award = 'Продукция собственных торговых марок «Макси» получила награды в 6 номинациях на 27-й Международной выставке «Продэкспо-2020».'

    def menu_link_history(self):
        p = ss('.navigation-link').filtered_by(have.text("Официально")).element(0)
        p.hover()
        s("a[href='/history']").should(be.visible).click()
        assert browser.driver.current_url == 'https://maxitest.ru/history'

    def test_history_view(self):
        self.menu_link_history()
        image = ss('.history-block__info-block .radius').should(be.visible).element(0)
        #assert image.get(query.attribute('src')) == 'https://maxitest.ru/api/resources/STATIC/HISTORY/history-2020-1.jpeg'
        #text = ss('.history-block__text-block p').element(0)
        #assert text.get(query.text) == self.award

