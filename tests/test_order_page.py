import allure
import pytest
from pages.order_page import OrderPage
from data import get_test_data_for_success_order, set_test_data_for_success_order


class TestOrderScooter:
    driver = None

    @allure.title('Тест на проверку успешного заказа самоката # {set_number} на сайте '
                  'https://qa-scooter.praktikum-services.ru/')
    @pytest.mark.parametrize('set_number', [1, 2])
    def test_success_order_of_scooter(self, set_number, driver):
        self.driver = driver

        order_page = OrderPage(self.driver)
        set_data = set_test_data_for_success_order(set_number)
        order_page.wait_for_load_home_page()
        order_page.click_cookies_button()

        order_page.click_order_button_main_page(get_test_data_for_success_order('Order_button', set_data))
        order_page.fill_data_first_page(set_data)
        order_page.click_on_next_button()

        order_page.wait_for_load_home_page()

        order_page.fill_data_second_page(set_data)
        order_page.click_order_button_order_page()
        order_page.click_yes_button_order_popup()

        status_text = order_page.check_success_ordering()
        assert 'Заказ оформлен' in status_text, 'Статус некорректный'

    @allure.title('Тест на проверку успешной загрузки стартовой страницы после клика на Лого на сайте '
                  'https://qa-scooter.praktikum-services.ru/')
    def test_success_loading_page_after_clicking_on_logo(self, driver):
        self.driver = driver

        order_page = OrderPage(self.driver)
        order_page.wait_for_load_home_page()
        order_page.click_logo_button()
        order_page.wait_for_load_home_page()
        header_text = order_page.check_start_page()
        assert 'Самокат' in header_text, 'Главная страница не загрузилась'

    @allure.title('Тест на проверку успешной загрузки страницы Дзена после клика на Яндекс Лого на сайте '
                      'https://qa-scooter.praktikum-services.ru/')
    def test_success_loading_page_after_clicking_on_ya_logo(self, driver):
        self.driver = driver

        order_page = OrderPage(self.driver)
        order_page.wait_for_load_home_page()
        order_page.click_yandex_button()
        order_page.wait_for_load_home_page()
        number_of_tabs = order_page.check_new_tab_open()
        assert number_of_tabs > 1, 'Новая вкладка не открылась'
        order_page.go_to_new_tab()
        order_page.click_ok_button_on_dzen()
        current_url = order_page.check_new_tab_url()
        assert 'dzen.ru' in current_url, 'Новая вкладка имеет некорректный url'
        order_page.close_old_pages()
