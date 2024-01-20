from pages.language_change_to_english import language_change
import allure


def test_language_change():

    with allure.step('Открываем тестируемую форму https://12go.asia/en'):
        language_change.open()

    with allure.step('Меняем язык сайта на Английский'):
        language_change.language_change()

    with allure.step('Проверяем смену языка'):
        language_change.assert_language_change()
