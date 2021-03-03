from selene import be
from selene.support import by
from selene.support.shared.jquery_style import s, ss

from base_test import BaseTest


class TestProfileEdit(BaseTest):

    is_private_phone_select = False
    is_show_birthday_select = False

    def test_profile_edit(self):
        s('.user-name').click()
        s('.user__personal-editBtn').should(be.visible).click()
        assert len(ss('.cbx')) == 2
        self.show_private_phone(ss('.cbx').element(0))
        s('#birthdayMask').click().set_value('27101995')
        self.show_birthday(ss('.cbx').element(1))
        s('#viber').click().set_value('1234567890')
        s('#whatsapp').click().set_value('1234567890')
        s('#skype').set_value('1234567890')
        s('#vk').set_value('12345678901234567890')
        s('#fb').set_value('12345678901234567890')
        s('#web').set_value('12345678901234567890')
        s('#zone').set_value('ectetur adipiscing elit aliqua. Ut enim ad minim veniam, quis nostrud exercitatip ex lor in rnulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
        s('.main-btn_primary').click()
        assert len(ss('.cbx')) == 0

    def test_profile_check(self):
        s('.user-name').click()
        if self.is_private_phone_select:
            s(by.text('Личный телефон:')).should(be.visible)
        else:
            assert len(ss(by.text('Личный телефон:'))) == 0

        # if self.is_show_birthday_select:
        #     s(by.text('День рождения:')).should(be.visible)
        # else:
        #     assert len(ss(by.text('День рождения:'))) == 0


    def show_private_phone(self, cbx):
        if cbx.get_attribute('class') == 'cbx active':
            self.is_private_phone_select = True
        else:
            self.is_private_phone_select = False


    def show_birthday(self, cbx):
        if cbx.get_attribute('class') == 'cbx active':
            self.is_show_birthday_select = True
        else:
            self.is_show_birthday_select = False
