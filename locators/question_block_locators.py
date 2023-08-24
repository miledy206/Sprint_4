from selenium.webdriver.common.by import By


class Questions:

    FIND_QUESTION_0 = [By.XPATH, './/div[@id = "accordion__heading-0"]']
    FIND_QUESTION_1 = [By.XPATH, './/div[@id = "accordion__heading-1"]']
    FIND_QUESTION_2 = [By.XPATH, './/div[@id = "accordion__heading-2"]']
    FIND_QUESTION_3 = [By.XPATH, './/div[@id = "accordion__heading-3"]']
    FIND_QUESTION_4 = [By.XPATH, './/div[@id = "accordion__heading-4"]']
    FIND_QUESTION_5 = [By.XPATH, './/div[@id = "accordion__heading-5"]']
    FIND_QUESTION_6 = [By.XPATH, './/div[@id = "accordion__heading-6"]']
    FIND_QUESTION_7 = [By.XPATH, './/div[@id = "accordion__heading-7"]']


class Answers:
    FIND_ANSWER_0 = [By.XPATH, './/div[@id = "accordion__heading-0"]/parent::div/parent::div/div[@id = '
                               '"accordion__panel-0" and not(@hidden)]/p']
    FIND_ANSWER_1 = [By.XPATH, './/div[@id = "accordion__heading-1"]/parent::div/parent::div/div[@id = '
                               '"accordion__panel-1" and not(@hidden)]/p']
    FIND_ANSWER_2 = [By.XPATH, './/div[@id = "accordion__heading-2"]/parent::div/parent::div/div[@id = '
                               '"accordion__panel-2" and not(@hidden)]/p']
    FIND_ANSWER_3 = [By.XPATH, './/div[@id = "accordion__heading-3"]/parent::div/parent::div/div[@id = '
                               '"accordion__panel-3" and not(@hidden)]/p']
    FIND_ANSWER_4 = [By.XPATH, './/div[@id = "accordion__heading-4"]/parent::div/parent::div/div[@id = '
                               '"accordion__panel-4" and not(@hidden)]/p']
    FIND_ANSWER_5 = [By.XPATH, './/div[@id = "accordion__heading-5"]/parent::div/parent::div/div[@id = '
                               '"accordion__panel-5" and not(@hidden)]/p']
    FIND_ANSWER_6 = [By.XPATH, './/div[@id = "accordion__heading-6"]/parent::div/parent::div/div[@id = '
                               '"accordion__panel-6" and not(@hidden)]/p']
    FIND_ANSWER_7 = [By.XPATH, './/div[@id = "accordion__heading-7"]/parent::div/parent::div/div[@id = '
                               '"accordion__panel-7" and not(@hidden)]/p']


class Buttons:
    FIND_COOKIES_BUTTON = [By.XPATH, './/button[contains(text(), "да все привыкли")]']
    FIND_QUESTION_BLOCK = [By.XPATH, './/div[contains(text(), "Вопросы о важном")]']
