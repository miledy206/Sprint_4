import allure
from selenium.common import NoSuchElementException, TimeoutException

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page_locators import Buttons, Fields


class OrderPage:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    # Метод нажатия на кнопку "Заказать" в шапке
    @allure.step('Нажать на кнопку "Заказать"')
    def click_order_button_main_page(self, select_button):
        if select_button == 'header':
            self.driver.find_element(*Buttons.FIND_ORDER_BUTTON_HEADER_MAIN_PAGE).click()
        else:
            self.driver.find_element(*Buttons.FIND_ORDER_BUTTON_MAIN_PAGE).click()

    # Метод для подтверждения кнопки куков
    @allure.step('Подтвердить использование куков на сайте')
    def click_cookies_button(self):
        try:
            self.driver.find_element(*Buttons.FIND_COOKIES_BUTTON).click()
        except NoSuchElementException:
            return False
        return True

    # Методы для первой страницы заказа
    @allure.step('Заполнить поле "Имя" в форме')
    def fill_name_field(self, name):
        return self.driver.find_element(*Fields.FIND_NAME_FIELD).send_keys(name)

    @allure.step('Заполнить поле "Фамилия" в форме')
    def fill_surname_field(self, surname):
        return self.driver.find_element(*Fields.FIND_SURNAME_FIELD).send_keys(surname)

    @allure.step('Заполнить поле "Адрес" в форме')
    def fill_address_field(self, address):
        return self.driver.find_element(*Fields.FIND_ADDRESS_FIELD).send_keys(address)

    @allure.step('Найти ближайшую к адресу станцию метро')
    def select_metro_station(self, station, set_number):
        self.driver.find_element(*Fields.FIND_STATION_FIELD).send_keys(station)
        self.driver.find_element(*Fields.set_select_metro_station(set_number)).click()

    @allure.step('Заполнить поле "Телефон" в форме')
    def fill_phone_number(self, phone):
        return self.driver.find_element(*Fields.FIND_PHONE_FIELD).send_keys(phone)

    @allure.step('Перейти на второй шаг заполнения формы')
    def click_on_next_button(self):
        self.driver.find_element(*Buttons.FIND_NEXT_BUTTON).click()

    # Методы для второй страницы заказа
    @allure.step('Выбрать дату подачи')
    def select_date(self):
        self.driver.find_element(*Fields.FIND_CALENDAR_FIELD).click()
        self.driver.find_element(*Fields.CLICK_DATEPICKER).click()

    @allure.step('Выбрать период аренды')
    def select_rent_period(self, set_number):
        self.driver.find_element(*Fields.FIND_RENT_FIELD).click()
        self.driver.find_element(*Fields.set_select_rent_value(set_number)).click()

    @allure.step('Выбрать цвет самоката')
    def select_colour(self, set_number):
        self.driver.find_element(*Fields.set_scooter_colour(set_number)).click()

    @allure.step('Заполнить поле "Комментарий" в форме')
    def fill_comment(self, comment):
        self.driver.find_element(*Fields.FIND_COMMENT_FIELD).send_keys(comment)

    # Метод нажатия на кнопку "Заказать" в заказе
    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button_order_page(self):
        self.driver.find_element(*Buttons.FIND_ORDER_BUTTON_ORDER_PAGE).click()

    # Метод нажатия на кнопку "Да" в модалке
    @allure.step('Подтвердить заказ')
    def click_yes_button_order_popup(self):
        self.driver.find_element(*Buttons.FIND_YES_BUTTON_ORDER_POPUP).click()

    # Метод проверки успешности заказа
    @allure.step('Проверить, что заказ создан успешно')
    def check_success_ordering(self):
        status = self.driver.find_element(*Fields.FIND_STATUS_OF_ORDER)
        status_text = status.get_attribute('innerText')
        assert 'Заказ оформлен' in status_text, 'Статус некорректный'

    @allure.step('Закрыть модальное окно с результатом заказа')
    def click_check_status_button_order_popup(self):
        self.driver.find_element(*Buttons.FIND_CHECK_STATUS_BUTTON_ORDER_POPUP).click()

    @allure.step('Подождать загрузку формы')
    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            Fields.FIND_LOGO))

    # Проверки открытия главной страницы и новой вкладки
    @allure.step('Кликнуть на лого сайта')
    def click_logo_button(self):
        self.driver.find_element(*Fields.FIND_LOGO).click()

    @allure.step('Проверить, что стартовая страница загрузилась')
    def check_start_page(self):
        header = self.driver.find_element(*Fields.FIND_HEADER_MAIN_PAGE)
        header_text = header.get_attribute('innerText')
        assert 'Самокат' in header_text, 'Главная страница не загрузилась'

    @allure.step('Кликнуть на Яндекс')
    def click_yandex_button(self):
        self.driver.find_element(*Fields.FIND_YANDEX).click()

    @allure.step('Проверить, что новая страница открылась')
    def check_new_tab_open(self):
        assert len(self.driver.window_handles) > 1, 'Новая вкладка не открылась'

    @allure.step('Переключиться на новую вкладку')
    def go_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Закрыть попап на странице Дзена')
    def click_ok_button_on_dzen(self):
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
                Fields.FIND_CLOSE_BUTTON_POPUP_DZEN)).click()
        except TimeoutException:
            return False
        return True

    @allure.step('Проверить, что новая вкладка ведёт на Дзен')
    def check_new_tab_url(self):
        assert 'dzen.ru' in self.driver.current_url, 'Новая вкладка имеет некорректный url'

    @allure.step('Закрыть неиспользуемую вкладку')
    def close_old_pages(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
