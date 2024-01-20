import allure
from pages.footer_follow_link_terms import footer_terms


def test_link_about_us():
    with allure.step('Открываем тестируемую форму https://12go.asia/en'):
        footer_terms.open()

    with allure.step('Переходим по ссылке Terms and Conditions'):
        footer_terms.follow_link()

    with allure.step('Проверяем правильность перехода'):
        footer_terms.assert_follow_link()
