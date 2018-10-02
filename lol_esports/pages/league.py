"""Classes and functionalities for each League (aka Competitions) Page.

Each League has four pages and is represented with a Page and PageMap class:
    * Schedule (the League "home" or "landing" page)
    * Teams & Standings
    * Stats
    * About

Classes
--------
* LeaguePage
* LeaguePageMap

Usage
------
code-example::
    league = LeaguePage(driver)
    league.goto('NA LCS')
    assert league.map.schedule_tab.is_displayed
"""

__author__ = "Carlos Kidman"


from framework.drivercore import by
from framework.drivercore import waitconditions as conditions
from lol_esports.pages.pagebase import PageBase


class LeaguePage(PageBase):
    """The League Page implementation.
    
    After selecting the League to goto(), the Schedule subpage
    is loaded with the Schedule Tab selected and active.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self.map = LeaguePageMap(driver)

    def goto(self, league):
        """Go to the specified League's page.
        
        Arguments
        ----------
        * league (str): the name of the League.

        Examples
        ----------
        - pages.league.goto("NA LCS")
        - pages.league.goto("LCK")
        - pages.league.goto("World Championship")
        """
        self.goto_league(league)
        self.wait_for_page_load()

    def wait_for_page_load(self):
        self._driver.wait.until(
            conditions.element_displayed(self.map.schedule_tab))


class LeaguePageMap:
    def __init__(self, driver):
        self._driver = driver

    @property
    def league_nav_container(self):
        return self._driver.find_element(by.css('.league-nav-container'))

    @property
    def schedule_tab(self):
        return self._driver.find_element(by.xpath('(//a[@href="/en_US/na-lcs/na_2018_summer/schedule"])[2]'))

    @property
    def schedule_container(self):
        return self._driver.find_element(by.id('schedule'))
