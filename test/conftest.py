import pytest
from selene.support.shared import browser
from selenium import webdriver
from util import attach


@pytest.fixture(scope="module",autouse = True )
def setup_browser():
    options = webdriver.ChromeOptions()
    options.browser_version = "100"

    # Headless
    # options.add_argument('--headless=new')

    options.set_capability(
        'selenoid:options',
         {
            "enableVNC": True,
            "enableVideo": True
        }
    )
    # browser.config.driver_options = options
    # browser.config.driver_remote_url = (
    #     "http://95.216.214.178:8080/wd/hub"
    # )
    browser.config.driver_remote_url = (
        "https://user1:1234@selenoid.autotests.cloud/wd/hub"
    )

    browser.config.base_url = 'https://test-dev.v5-pre.pryaniky.com'
    browser.config.timeout = 30
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add__screenshot(browser)
    attach.add_video(browser)
    browser.quit()
