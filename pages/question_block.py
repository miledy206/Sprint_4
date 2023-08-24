import allure
from selenium.common import NoSuchElementException

from locators.question_block_locators import Questions, Answers, Buttons
from test_data import get_question_by_id


class QuestionBlock:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подтвердить использование куков на сайте, если необходимо')
    def click_cookies_button(self):
        try:
            self.driver.find_element(*Buttons.FIND_COOKIES_BUTTON).click()
        except NoSuchElementException:
            return False
        return True

    @allure.step('Раскрыть первый вопрос')
    def click_on_question_0(self):
        self.driver.find_element(*Questions.FIND_QUESTION_0).click()

    @allure.step('Проверить ответ на первый вопрос')
    def check_answer_0(self):
        element = self.driver.find_element(*Answers.FIND_ANSWER_0).get_attribute('innerText')
        assert element == get_question_by_id('question_0'), 'Ответ скрыт или отсутствует'

    @allure.step('Раскрыть второй вопрос')
    def click_on_question_1(self):
        self.driver.find_element(*Questions.FIND_QUESTION_1).click()

    @allure.step('Проверить ответ на второй вопрос')
    def check_answer_1(self):
        element = self.driver.find_element(*Answers.FIND_ANSWER_1).get_attribute('innerText')
        assert element == get_question_by_id('question_1'), 'Ответ скрыт или отсутствует'

    @allure.step('Раскрыть третий вопрос')
    def click_on_question_2(self):
        self.driver.find_element(*Questions.FIND_QUESTION_2).click()

    @allure.step('Проверить ответ на третий вопрос')
    def check_answer_2(self):
        element = self.driver.find_element(*Answers.FIND_ANSWER_2).get_attribute('innerText')
        assert element == get_question_by_id('question_2'), 'Ответ скрыт или отсутствует'

    @allure.step('Раскрыть четвёртый вопрос')
    def click_on_question_3(self):
        self.driver.find_element(*Questions.FIND_QUESTION_3).click()

    @allure.step('Проверить ответ на четвёртый вопрос')
    def check_answer_3(self):
        element = self.driver.find_element(*Answers.FIND_ANSWER_3).get_attribute('innerText')
        assert element == get_question_by_id('question_3'), 'Ответ скрыт или отсутствует'

    @allure.step('Раскрыть пятый вопрос')
    def click_on_question_4(self):
        self.driver.find_element(*Questions.FIND_QUESTION_4).click()

    @allure.step('Проверить ответ на пятый вопрос')
    def check_answer_4(self):
        element = self.driver.find_element(*Answers.FIND_ANSWER_4).get_attribute('innerText')
        assert element == get_question_by_id('question_4'), 'Ответ скрыт или отсутствует'

    @allure.step('Раскрыть шестой вопрос')
    def click_on_question_5(self):
        self.driver.find_element(*Questions.FIND_QUESTION_5).click()

    @allure.step('Проверить ответ на шестой вопрос')
    def check_answer_5(self):
        element = self.driver.find_element(*Answers.FIND_ANSWER_5).get_attribute('innerText')
        assert element == get_question_by_id('question_5'), 'Ответ скрыт или отсутствует'

    @allure.step('Раскрыть седьмой вопрос')
    def click_on_question_6(self):
        self.driver.find_element(*Questions.FIND_QUESTION_6).click()

    @allure.step('Проверить ответ на седьмой вопрос')
    def check_answer_6(self):
        element = self.driver.find_element(*Answers.FIND_ANSWER_6).get_attribute('innerText')
        assert element == get_question_by_id('question_6'), 'Ответ скрыт или отсутствует'

    @allure.step('Раскрыть восьмой вопрос')
    def click_on_question_7(self):
        self.driver.find_element(*Questions.FIND_QUESTION_7).click()

    @allure.step('Проверить ответ на восьмой вопрос')
    def check_answer_7(self):
        element = self.driver.find_element(*Answers.FIND_ANSWER_7).get_attribute('innerText')
        assert element == get_question_by_id('question_7'), 'Ответ скрыт или отсутствует'

    def click_question_selectors(self, question_number):
        # метод определения, какой вопрос сейчас нужно проверить
        if question_number == 1:
            self.click_on_question_0()
        elif question_number == 2:
            self.click_on_question_1()
        elif question_number == 3:
            self.click_on_question_2()
        elif question_number == 4:
            self.click_on_question_3()
        elif question_number == 5:
            self.click_on_question_4()
        elif question_number == 6:
            self.click_on_question_5()
        elif question_number == 7:
            self.click_on_question_6()
        else:
            self.click_on_question_7()

    def check_answer_selectors(self, question_number):
        # метод определения, какой ответ сейчас нужно проверить
        if question_number == 1:
            self.check_answer_0()
        elif question_number == 2:
            self.check_answer_1()
        elif question_number == 3:
            self.check_answer_2()
        elif question_number == 4:
            self.check_answer_3()
        elif question_number == 5:
            self.check_answer_4()
        elif question_number == 6:
            self.check_answer_5()
        elif question_number == 7:
            self.check_answer_6()
        else:
            self.check_answer_7()
