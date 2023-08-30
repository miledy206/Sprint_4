from data import set_list_of_questions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

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
