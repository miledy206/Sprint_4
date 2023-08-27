from selenium.webdriver.common.by import By
from data import get_test_data_for_success_order


class Buttons:
    FIND_ORDER_BUTTON_HEADER_MAIN_PAGE = [By.XPATH, './/div[contains(@class, "Header")]/button[text() = "Заказать"]']
    FIND_ORDER_BUTTON_MAIN_PAGE = [By.XPATH,
                                   './/div[contains(@class, "Home_FinishButton")]/button[text() = "Заказать"]']
    FIND_NEXT_BUTTON = [By.XPATH, './/button[text() = "Далее"]']
    FIND_ORDER_BUTTON_ORDER_PAGE = [By.XPATH, './/div[contains(@class, "Order_Buttons")]/button[text() = "Заказать"]']
    FIND_YES_BUTTON_ORDER_POPUP = [By.XPATH, './/div[contains(@class, "Order_Modal")]//button[text() = "Да"]']
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
                f'.//div[text() ="{get_test_data_for_success_order("Metro_station", set_number)}"]/parent::button']

    FIND_PHONE_FIELD = [By.XPATH, './/input[contains(@placeholder, "Телефон")]']

    # Поля на второй странице Заказа
    FIND_CALENDAR_FIELD = [By.XPATH, './/input[contains(@placeholder, "Когда привезти самокат")]']
    CLICK_DATEPICKER = [By.XPATH, './/div[contains(@class, "react-datepicker__month-container")]']
    FIND_RENT_FIELD = [By.XPATH, './/div[text() = "* Срок аренды"]']

    @staticmethod
    def set_select_rent_value(set_number):
        return [By.XPATH, f'.//div[contains(text(), "{get_test_data_for_success_order("Rent", set_number)}")]']

    @staticmethod
    def set_scooter_colour(set_number):
        return [By.XPATH, f'.//label[@for = "{get_test_data_for_success_order("Label", set_number)}"]/input']

    FIND_COMMENT_FIELD = [By.XPATH, './/input[contains(@placeholder, "Комментарий")]']

    # Финальная страница с заказом
    FIND_STATUS_OF_ORDER = [By.XPATH,
                            './/div[contains(@class, "Order_ModalHeader")]']
