"""Classes and functionalities for the Home Page.

NOTE:
    Since the Home Page is the most common starting place for the
    lolesports.com tests, it is usually part of "Step 1 - go to lolesports.com".

Classes
--------
* HomePage
* HomePageMap

Usage
------
code-example::
    driver.goto("https://www.lolesports.com")
    home = HomePage(driver)
    home.wait_for_page_load()
    assert home.basemap.main_navbar_tab("HOME").is_displayed
"""

__author__ = "Carlos Kidman"


from framework.drivercore import by
from framework.drivercore import waitconditions as conditions
from lol_esports.pages.pagebase import PageBase


class HomePage(PageBase):
    """The Home Page implementation."""

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
        self._driver.wait.until(conditions.element_displayed(self.basemap.main_navbar_tab("HOME")))


class HomePageMap:
    def __init__(self, driver):
        self._driver = driver
