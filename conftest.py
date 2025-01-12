import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os

driver: webdriver.Remote

@pytest.fixture
def setup_teardown():
    #setup
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get('https://www.demoblaze.com/')

    #executa o teste que foi chamado
    yield

    #teardown
    driver.quit()
