import allure

from locators.question_block_locators import Questions, Answers
from pages.base_page import BasePage


class QuestionBlock(BasePage):

    @allure.step('Раскрыть первый вопрос')
    def click_on_question_0(self):
        self.click_on_element(Questions.FIND_QUESTION_0)

    @allure.step('Проверить ответ на первый вопрос')
    def check_answer_0(self):
        element = self.get_attribute_of_field(Answers.FIND_ANSWER_0, 'innerText')
        return element

    @allure.step('Раскрыть второй вопрос')
    def click_on_question_1(self):
        self.click_on_element(Questions.FIND_QUESTION_1)

    @allure.step('Проверить ответ на второй вопрос')
    def check_answer_1(self):
        element = self.get_attribute_of_field(Answers.FIND_ANSWER_1, 'innerText')
        return element

    @allure.step('Раскрыть третий вопрос')
    def click_on_question_2(self):
        self.click_on_element(Questions.FIND_QUESTION_2)

    @allure.step('Проверить ответ на третий вопрос')
    def check_answer_2(self):
        element = self.get_attribute_of_field(Answers.FIND_ANSWER_2, 'innerText')
        return element

    @allure.step('Раскрыть четвёртый вопрос')
    def click_on_question_3(self):
        self.click_on_element(Questions.FIND_QUESTION_3)

    @allure.step('Проверить ответ на четвёртый вопрос')
    def check_answer_3(self):
        element = self.get_attribute_of_field(Answers.FIND_ANSWER_3, 'innerText')
        return element

    @allure.step('Раскрыть пятый вопрос')
    def click_on_question_4(self):
        self.click_on_element(Questions.FIND_QUESTION_4)

    @allure.step('Проверить ответ на пятый вопрос')
    def check_answer_4(self):
        element = self.get_attribute_of_field(Answers.FIND_ANSWER_4, 'innerText')
        return element

    @allure.step('Раскрыть шестой вопрос')
    def click_on_question_5(self):
        self.click_on_element(Questions.FIND_QUESTION_5)

    @allure.step('Проверить ответ на шестой вопрос')
    def check_answer_5(self):
        element = self.get_attribute_of_field(Answers.FIND_ANSWER_5, 'innerText')
        return element

    @allure.step('Раскрыть седьмой вопрос')
    def click_on_question_6(self):
        self.click_on_element(Questions.FIND_QUESTION_6)

    @allure.step('Проверить ответ на седьмой вопрос')
    def check_answer_6(self):
        element = self.get_attribute_of_field(Answers.FIND_ANSWER_6, 'innerText')
        return element

    @allure.step('Раскрыть восьмой вопрос')
    def click_on_question_7(self):
        self.click_on_element(Questions.FIND_QUESTION_7)

    @allure.step('Проверить ответ на восьмой вопрос')
    def check_answer_7(self):
        element = self.get_attribute_of_field(Answers.FIND_ANSWER_7, 'innerText')
        return element

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
            return self.check_answer_0()
        elif question_number == 2:
            return self.check_answer_1()
        elif question_number == 3:
            return self.check_answer_2()
        elif question_number == 4:
            return self.check_answer_3()
        elif question_number == 5:
            return self.check_answer_4()
        elif question_number == 6:
            return self.check_answer_5()
        elif question_number == 7:
            return self.check_answer_6()
        else:
            return self.check_answer_7()

