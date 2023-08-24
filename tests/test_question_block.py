import allure
import pytest
from selenium import webdriver
from pages.question_block import QuestionBlock


class TestQnA:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Тест на проверку вопроса и ответа № {question_number} на главной странице сайта '
                  'https://qa-scooter.praktikum-services.ru/')
    @pytest.mark.parametrize('question_number', [1, 2, 3, 4, 5, 6, 7, 8])
    def test_answer_on_question(self, question_number):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        self.driver.maximize_window()

        question_block = QuestionBlock(self.driver)
        question_block.click_cookies_button()

        question_block.click_question_selectors(question_number)
        question_block.check_answer_selectors(question_number)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

