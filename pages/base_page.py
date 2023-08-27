import allure
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import Buttons


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подтвердить использование куков на сайте, если необходимо')
    def click_cookies_button(self):
        try:
            self.driver.find_element(*Buttons.FIND_COOKIES_BUTTON).click()
        except NoSuchElementException:
            return False
        return True

    def click_on_element(self, locator):
        # метод для нажатия на любой элемент на странице
        return self.driver.find_element(*locator).click()

    def send_value_to_field(self, locator, key):
        # метод для заполнения любого поля на странице
        search_field = self.driver.find_element(*locator)
        search_field.click()
        search_field.send_keys(key)
        return search_field

    def get_attribute_of_field(self, locator, attribute):
        # метод для определения атрибута элемента на странице
        return self.driver.find_element(*locator).get_attribute(attribute)

    @allure.step('Подождать загрузку формы')
    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            Buttons.FIND_LOGO))

    @allure.step('Переключиться на новую вкладку')
    def go_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Закрыть неиспользуемую вкладку')
    def close_old_pages(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    @allure.step('Закрыть попап на странице Дзена')
    def click_ok_button_on_dzen(self):
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
                Buttons.FIND_CLOSE_BUTTON_POPUP_DZEN)).click()
        except TimeoutException:
            return False
        return True

    @allure.step('Кликнуть на Яндекс')
    def click_yandex_button(self):
        self.click_on_element(Buttons.FIND_YANDEX)

    # Проверки открытия главной страницы и новой вкладки
    @allure.step('Кликнуть на лого сайта')
    def click_logo_button(self):
        self.click_on_element(Buttons.FIND_LOGO)

    @allure.step('Проверить, что стартовая страница загрузилась')
    def check_start_page(self):
        header_text = self.get_attribute_of_field(Buttons.FIND_HEADER_MAIN_PAGE, 'innerText')
        return header_text

    @allure.step('Проверить, что новая страница открылась')
    def check_new_tab_open(self):
        number_of_tabs = len(self.driver.window_handles)
        return number_of_tabs

    @allure.step('Проверить, что новая вкладка ведёт на Дзен')
    def check_new_tab_url(self):
        current_url = self.driver.current_url
        return current_url
