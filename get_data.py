# Запросы в тестовые данные
from data import set_list_of_questions


def get_question_by_id(field):
    # метод вытаскивания ответа для определённого вопроса
    questions_list = set_list_of_questions()

    return questions_list.get(field)


def get_test_data_for_success_order(field, set_data):
    # метод вытаскивания значения для определённого поля в выбранном сете
    return set_data.get(field)
