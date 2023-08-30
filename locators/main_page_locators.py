from selenium.webdriver.common.by import By


class Buttons:

    FIND_COOKIES_BUTTON = [By.XPATH, './/button[contains(text(), "да все привыкли")]']

    # Logo and yandex
    FIND_LOGO = [By.XPATH, './/a[contains(@class, "Header_LogoScooter")]']
    FIND_YANDEX = [By.XPATH, './/a[contains(@class, "Header_LogoYandex")]']

    # Helping locators
    FIND_HEADER_MAIN_PAGE = [By.XPATH, './/div[contains(@class, "Home_Header")]']
    FIND_CLOSE_BUTTON_POPUP_DZEN = [By.XPATH, './/span[@tabindex = "0"]']
