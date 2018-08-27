import unittest
from selenium.webdriver.support.ui import WebDriverWait
from framework.driver_core.driver import Driver
from league_esports.page_objects.page_controller import Pages


class UnitTests(unittest.TestCase):

    def test_selenium_is_up_and_running(self):
        driver = Driver("chrome")
        wait = WebDriverWait(driver, 30)
        pages = Pages(driver, wait)

        driver.goto("https://www.lolesports.com")
        pages.home.wait_for_page_load()
        pages.league.goto()

        assert driver.title == "Schedule | LoL Esports"


if __name__ == "__main__":
    unittest.main()
