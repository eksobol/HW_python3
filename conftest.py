import pytest
from selene import browser

@pytest.fixture(scope="session")
def browser_settings():
    browser.config.base_url = ("https://google.com/ncr")
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    print("Браузер google открыт!")

    yield

    print("Закрываем браузер!")
