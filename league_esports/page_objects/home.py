from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expect
from league_esports.page_objects.pagebase import PageBase


class HomePage(PageBase):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self._driver = driver
        self._wait = wait
        self.map = HomePageMap(driver)

    def goto(self):
        self.goto_home()
        self.wait_for_page_load()

    def wait_for_page_load(self):
        self._wait.until(expect.visibility_of(self.basemap.main_navbar_tab("HOME")))


class HomePageMap:
    def __init__(self, driver):
        self._driver = driver
