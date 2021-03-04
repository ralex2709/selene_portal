import time

from selene import be, query
from selene.support import by
from selene.support.shared.jquery_style import s, ss

from base_test import BaseTest
from helpers.string_helper import randomworld


class TestProfileEdit(BaseTest):

    is_private_phone_select = False
    is_show_birthday_select = False
    skype = 'skype'
    vk = 'vk'
    fb = 'Fb'
    web = 'web'
    work = 'work'

    def test_profile_edit(self):
        s('.user-name').click()
        s('.user__personal-editBtn').should(be.visible).click()
        assert len(ss('.cbx')) == 2
        self.show_private_phone(ss('.cbx').element(0))
        s('#birthdayMask').clear().click().set_value('27101998')
        self.show_birthday(ss('.cbx').element(1))
        s('#viber').click().set_value('1234567890')
        s('#whatsapp').click().set_value('1234567890')
        s('#skype').set_value(self.skype)
        s('#vk').set_value(self.vk)
        s('#fb').set_value(self.fb)
        s('#web').set_value(self.web)
        s('#zone').set_value(self.work)
        self.save_profile()

    def test_profile_check(self):
        s('.user-name').click()
        if self.is_private_phone_select:
            s(by.text('Личный телефон:')).should(be.visible)
        else:
            assert len(ss(by.text('Личный телефон:'))) == 0

        s('.user__personal-editBtn').click()
        ss('.cbx').element(0).click()
        self.show_private_phone(ss('.cbx').element(0))
        self.save_profile()

        if self.is_private_phone_select:
            s(by.text('Личный телефон:')).should(be.visible)
        else:
            assert len(ss(by.text('Личный телефон:'))) == 0

        s(by.text('День рождения:')).should(be.visible)
        if self.is_show_birthday_select:
            s(by.text('27 октября')).should(be.visible)
        else:
            s(by.text('27 октября 1998')).should(be.visible)

        s('.user__personal-editBtn').click()
        s('#birthdayMask').should(be.visible).clear()
        self.save_profile()
        s(by.text('День рождения:')).should(be.hidden)
        s(by.text('Viber:')).should(be.visible)
        s(by.text('Whatsapp:')).should(be.visible)
        s(by.text(self.skype)).should(be.visible)
        s(by.text(self.vk)).should(be.visible)
        s(by.text(self.fb)).should(be.visible)
        s(by.text(self.web)).should(be.visible)
        s(by.text(self.work)).should(be.visible)

        s('.user__personal-editBtn').click()
        description_work = randomworld(255)
        s('#zone').set_value(description_work)
        self.save_profile()
        s(by.text(description_work)).should(be.visible)
        s('.user__personal-editBtn').click()
        description_work = randomworld(256)
        s('#zone').set_value(description_work)
        s('.main-btn_primary').click()
        s('.notification__msg.notification__msg_error.radius').should(be.visible)
        s('#zone').clear().set_value(self.work)
        self.save_profile()

    def save_profile(self):
        s('.main-btn_primary').click()
        ss('.cbx').should(be.hidden)

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
