"""Classes and functionalities for each League (aka Competitions) Page.

Each League has four pages and is represented with a Page and PageMap class:
    - Schedule (the League "home" or "landing" page)
    - Teams & Standings
    - Stats
    - About

Classes:
    - LeaguePage
    - LeaguePageMap

Usage:
    Only the Page classes should be instantiated in tests.
    The PageMap classes are consumed by their corresponding Page class.
    If you want to access the elements within the PageMap,
    use the "self.map" property through the Page instance.

Example:
    league = LeaguePage(driver, wait)
    league.goto("NA LCS")
    assert league.map.schedule_tab.is_displayed
"""

__author__ = "Carlos Kidman"

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expect
from lol_esports.pom.pagebase import PageBase


class LeaguePage(PageBase):
    """POM representing each League and its landing page - Schedule.
    
    After selecting the League to goto(), the Schedule subpage
    is loaded with the Schedule Tab selected and active.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self.map = LeaguePageMap(driver)

    def goto(self, league):
        """Go to the specified League's page.
        
        Args:
            - league (str): the name of the League.

        Example:
            - pages.league.goto("NA LCS")
            - pages.league.goto("LCK")
            - pages.league.goto("World Championship")
        """
        self.goto_league(league)
        self.wait_for_page_load()

    def wait_for_page_load(self):
        self._driver.wait.until(expect.element_to_be_clickable(
            self.map.schedule_tab.locator))


class LeaguePageMap:
    def __init__(self, driver):
        self._driver = driver

    @property
    def league_nav_container(self):
        return self._driver.find_element(By.CSS_SELECTOR, ".league-nav-container")

    @property
    def schedule_tab(self):
        return self._driver.find_element(By.XPATH, "(//a[@href='/en_US/na-lcs/na_2018_summer/schedule'])[2]")

    @property
    def schedule_container(self):
        return self._driver.find_element(By.ID, "schedule")
