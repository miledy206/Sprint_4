from selenium.webdriver.common.by import By
from test_data import get_test_data_for_success_order


class Buttons:
    FIND_ORDER_BUTTON_HEADER_MAIN_PAGE = [By.XPATH, './/div[contains(@class, "Header")]/button[text() = "Заказать"]']
    FIND_ORDER_BUTTON_MAIN_PAGE = [By.XPATH,
                                   './/div[contains(@class, "Home_FinishButton")]/button[text() = "Заказать"]']
    FIND_NEXT_BUTTON = [By.XPATH, './/button[text() = "Далее"]']
    FIND_ORDER_BUTTON_ORDER_PAGE = [By.XPATH, './/div[contains(@class, "Order_Buttons")]/button[text() = "Заказать"]']
    FIND_YES_BUTTON_ORDER_POPUP = [By.XPATH, './/div[contains(@class, "Order_Modal")]//button[text() = "Да"]']
    FIND_COOKIES_BUTTON = [By.XPATH, './/button[contains(text(), "да все привыкли")]']
    FIND_CHECK_STATUS_BUTTON_ORDER_POPUP = [By.XPATH, './/div[contains(@class, "Order_Modal")]//button[text() = '
                                                      '"Посмотреть статус"]']


class Fields:
    # Поля на первой странице Заказа
    FIND_NAME_FIELD = [By.XPATH, './/input[contains(@placeholder, "Имя")]']
    FIND_SURNAME_FIELD = [By.XPATH, './/input[contains(@placeholder, "Фамилия")]']
    FIND_ADDRESS_FIELD = [By.XPATH, './/input[contains(@placeholder, "Адрес")]']
    FIND_STATION_FIELD = [By.XPATH, './/input[contains(@placeholder, "Станция метро")]']

    @staticmethod
    def set_select_metro_station(set_number):
        return [By.XPATH,
                f'.//input[contains(@placeholder, "Станция метро")]/parent::div/parent::div/div//div[text() ="'
                f'{get_test_data_for_success_order("Metro_station", set_number)}"]/parent::button']

    FIND_PHONE_FIELD = [By.XPATH, './/input[contains(@placeholder, "Телефон")]']

    # Поля на второй странице Заказа
    FIND_CALENDAR_FIELD = [By.XPATH, './/input[contains(@placeholder, "Когда привезти самокат")]']
    CLICK_DATEPICKER = [By.XPATH, './/div[contains(@class, "react-datepicker__day") and contains(text(), "25")]']
    FIND_RENT_FIELD = [By.XPATH, './/div[text() = "* Срок аренды"]']

    @staticmethod
    def set_select_rent_value(set_number):
        return [By.XPATH, f'.//div[contains(text(), "Срок аренды")]/parent::div/parent::div//div[contains('
                          f'text(), "{get_test_data_for_success_order("Rent", set_number)}")]']

    @staticmethod
    def set_scooter_colour(set_number):
        return [By.XPATH, f'.//label[@for = "{get_test_data_for_success_order("Label", set_number)}"]/input']

    FIND_COMMENT_FIELD = [By.XPATH, './/input[contains(@placeholder, "Комментарий")]']

    # Финальная страница с заказом
    FIND_STATUS_OF_ORDER = [By.XPATH,
                            './/div[contains(@class, "Order_Modal")]//div[contains(@class, "Order_ModalHeader")]']

    # Logo and yandex
    FIND_LOGO = [By.XPATH, './/a[contains(@class, "Header_LogoScooter")]']
    FIND_YANDEX = [By.XPATH, './/a[contains(@class, "Header_LogoYandex")]']

    # Helping locators
    FIND_HEADER_MAIN_PAGE = [By.XPATH, './/div[contains(@class, "Home_Header")]']
    FIND_CLOSE_BUTTON_POPUP_DZEN = [By.XPATH, './/span[@tabindex = "0"]']
