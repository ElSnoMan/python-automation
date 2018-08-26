import unittest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, WebDriverException, StaleElementReferenceException
from league_esports.pages.home import HomePage
from league_esports.pages.league import LeaguePage


class UnitTests(unittest.TestCase):

    def test_selenium_is_up_and_running(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = Chrome("c:/dev/python-automation/_drivers/chromedriver.exe", chrome_options=options)
        wait = WebDriverWait(driver, 30)

        driver.get("https://www.lolesports.com")
        HomePage(driver, wait).wait_for_page_load()
        LeaguePage(driver, wait).goto()

        assert driver.title == "Schedule | LoL Esports"


if __name__ == "__main__":
    unittest.main()
