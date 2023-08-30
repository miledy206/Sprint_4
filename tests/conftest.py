import pytest
from selenium import webdriver

import data


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    start_url = data.start_url
    driver.get(start_url)
    driver.maximize_window()
    yield driver
    driver.quit()
