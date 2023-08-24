import allure
import pytest
from selenium import webdriver
from pages.order_page import OrderPage
from test_data import get_test_data_for_success_order, set_test_data_for_success_order


class TestOrderScooter:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Тест на проверку успешного заказа самоката # {set_number} на сайте '
                  'https://qa-scooter.praktikum-services.ru/')
    @pytest.mark.parametrize('set_number', [1, 2])
    def test_success_order_of_scooter(self, set_number):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        self.driver.maximize_window()

        order_page = OrderPage(self.driver)
        set_data = set_test_data_for_success_order(set_number)
        order_page.wait_for_load_home_page()
        order_page.click_cookies_button()

        order_page.click_order_button_main_page(get_test_data_for_success_order('Order_button', set_data))
        order_page.fill_name_field(get_test_data_for_success_order('Name', set_data))
        order_page.fill_surname_field(get_test_data_for_success_order('Surname', set_data))
        order_page.fill_address_field(get_test_data_for_success_order('Address', set_data))
        order_page.select_metro_station(get_test_data_for_success_order('Metro_station', set_data), set_data)
        order_page.fill_phone_number(get_test_data_for_success_order('Phone', set_data))
        order_page.click_on_next_button()

        order_page.wait_for_load_home_page()

        order_page.select_date()
        order_page.select_rent_period(set_data)
        order_page.select_colour(set_data)
        order_page.fill_comment(get_test_data_for_success_order('Comment', set_data))
        order_page.click_order_button_order_page()
        order_page.click_yes_button_order_popup()

        order_page.check_success_ordering()

        order_page.click_check_status_button_order_popup()
        order_page.wait_for_load_home_page()

        order_page.click_logo_button()
        order_page.wait_for_load_home_page()
        order_page.check_start_page()

        order_page.click_yandex_button()
        order_page.wait_for_load_home_page()
        order_page.check_new_tab_open()
        order_page.go_to_new_tab()
        order_page.click_ok_button_on_dzen()
        order_page.check_new_tab_url()
        order_page.close_old_pages()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
