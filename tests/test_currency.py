from pages.change_currency import ChangeCurrency
import allure


def test_currency():
    change_currency = ChangeCurrency()

    with allure.step('Открываем тестируемую форму https://12go.asia/en'):
        change_currency.open()

    with allure.step('Выбираем необходимую валюту'):
        change_currency.change_currency()

    with allure.step('Проверяем выбранную валюту'):
        change_currency.assert_currency()
