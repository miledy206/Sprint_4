import allure

from get_data import get_test_data_for_success_order
from locators.order_page_locators import Buttons, Fields
from pages.base_page import BasePage
from pages.main_page import MainPage


class OrderPage(MainPage):

    @allure.step('Нажать на кнопку "Заказать"')
    def click_order_button_main_page(self, select_button):
        if select_button == 'header':
            self.click_on_element(Buttons.FIND_ORDER_BUTTON_HEADER_MAIN_PAGE)
        else:
            self.click_on_element(Buttons.FIND_ORDER_BUTTON_MAIN_PAGE)

    # Методы для первой страницы заказа
    @allure.step('Заполнить поле "Имя" в форме')
    def fill_name_field(self, name):
        return self.send_value_to_field(Fields.FIND_NAME_FIELD, name)

    @allure.step('Заполнить поле "Фамилия" в форме')
    def fill_surname_field(self, surname):
        return self.send_value_to_field(Fields.FIND_SURNAME_FIELD, surname)

    @allure.step('Заполнить поле "Адрес" в форме')
    def fill_address_field(self, address):
        return self.send_value_to_field(Fields.FIND_ADDRESS_FIELD, address)

    @allure.step('Найти ближайшую к адресу станцию метро')
    def select_metro_station(self, station, set_number):
        self.send_value_to_field(Fields.FIND_STATION_FIELD, station)
        self.click_on_element(Fields.set_select_metro_station(set_number))

    @allure.step('Заполнить поле "Телефон" в форме')
    def fill_phone_number(self, phone):
        return self.send_value_to_field(Fields.FIND_PHONE_FIELD, phone)

    @allure.step('Перейти на второй шаг заполнения формы')
    def click_on_next_button(self):
        self.click_on_element(Buttons.FIND_NEXT_BUTTON)

    # Методы для второй страницы заказа
    @allure.step('Выбрать дату подачи')
    def select_date(self):
        self.click_on_element(Fields.FIND_CALENDAR_FIELD)
        self.click_on_element(Fields.CLICK_DATEPICKER)

    @allure.step('Выбрать период аренды')
    def select_rent_period(self, set_number):
        self.click_on_element(Fields.FIND_RENT_FIELD)
        self.click_on_element(Fields.set_select_rent_value(set_number))

    @allure.step('Выбрать цвет самоката')
    def select_colour(self, set_number):
        self.click_on_element(Fields.set_scooter_colour(set_number))

    @allure.step('Заполнить поле "Комментарий" в форме')
    def fill_comment(self, comment):
        self.send_value_to_field(Fields.FIND_COMMENT_FIELD, comment)

    # Метод нажатия на кнопку "Заказать" в заказе
    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button_order_page(self):
        self.click_on_element(Buttons.FIND_ORDER_BUTTON_ORDER_PAGE)

    # Метод нажатия на кнопку "Да" в модалке
    @allure.step('Подтвердить заказ')
    def click_yes_button_order_popup(self):
        self.click_on_element(Buttons.FIND_YES_BUTTON_ORDER_POPUP)

    def fill_data_first_page(self, set_data):
        # Метод заполнения полей в заказе для первой страницы
        self.fill_name_field(get_test_data_for_success_order('Name', set_data))
        self.fill_surname_field(get_test_data_for_success_order('Surname', set_data))
        self.fill_address_field(get_test_data_for_success_order('Address', set_data))
        self.select_metro_station(get_test_data_for_success_order('Metro_station', set_data), set_data)
        self.fill_phone_number(get_test_data_for_success_order('Phone', set_data))

    def fill_data_second_page(self, set_data):
        # Метод заполнения полей в заказе для второй страницы
        self.select_date()
        self.select_rent_period(set_data)
        self.select_colour(set_data)
        self.fill_comment(get_test_data_for_success_order('Comment', set_data))

    # Метод проверки успешности заказа
    @allure.step('Проверить, что заказ создан успешно')
    def check_success_ordering(self):
        status_text = self.get_attribute_of_field(Fields.FIND_STATUS_OF_ORDER, 'innerText')
        return status_text

