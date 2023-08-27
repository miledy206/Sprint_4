import allure
import pytest

from data import get_question_by_id
from pages.question_block import QuestionBlock


class TestQnA:

    driver = None

    @allure.title('Тест на проверку вопроса и ответа № {question_number} на главной странице сайта '
                  'https://qa-scooter.praktikum-services.ru/')
    @pytest.mark.parametrize('question_number', [1, 2, 3, 4, 5, 6, 7, 8])
    def test_answer_on_question(self, question_number, driver):

        self.driver = driver

        question_block = QuestionBlock(self.driver)
        question_block.click_cookies_button()

        question_block.click_question_selectors(question_number)
        element = question_block.check_answer_selectors(question_number)
        assert element == get_question_by_id(question_number), 'Ответ скрыт или отсутствует'

