import pytest
from selenium import webdriver

from data import get_start_url


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    start_url = get_start_url()
    driver.get(start_url)
    driver.maximize_window()
    yield driver
    driver.quit()
