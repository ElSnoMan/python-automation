"""Classes and functionalities for the Home Page.

NOTE:
    Since the Home Page is the most common starting place for the
    lolesports.com tests, it is usually part of "Step 1 - go to lolesports.com".

Classes:
    - HomePage
    - HomePageMap

Usage:
    Only the Page classes should be instantiated in tests.
    The PageMap classes are consumed by their corresponding Page class.
    If you want to access the elements within the PageMap,
    use the "self.map" property through the Page instance.

Example:
    driver.get("https://www.lolesports.com")
    home = HomePage(driver, wait)
    home.wait_for_page_load()
    assert home.basemap.main_navbar_tab("HOME").is_displayed
"""

__author__ = "Carlos Kidman"

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expect
from lol_esports.pom.pagebase import PageBase


class HomePage(PageBase):
    """POM representing the Home Page."""

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self.map = HomePageMap(driver)

    def goto(self):
        """Go to the Home Page.
        
        NOTE:
            This clicks on the Home Tab to get you to the Home Page.
            Call wait_for_page_load() if you are using driver
            to get to this page.
        """
        self.goto_home()
        self.wait_for_page_load()

    def wait_for_page_load(self):
        self._driver.wait.until(expect.visibility_of(self.basemap.main_navbar_tab("HOME")))


class HomePageMap:
    def __init__(self, driver):
        self._driver = driver
