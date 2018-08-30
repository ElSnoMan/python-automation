import unittest
from selenium.webdriver.support.ui import WebDriverWait
from framework.drivercore.driver import Driver
from lol_esports.pom.controller import Pages


class UnitTests(unittest.TestCase):

    def test_selenium_is_up_and_running(self):
        driver = Driver("chrome")
        wait = WebDriverWait(driver, 30)
        pages = Pages(driver, wait)

        driver.goto("https://www.lolesports.com")
        pages.home.wait_for_page_load()
        pages.league.goto("NA LCS")

        assert driver.title == "Schedule | LoL Esports"


if __name__ == "__main__":
    unittest.main()
