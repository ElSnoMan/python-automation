"""Controller that holds all the page objects.

Each website consists of pages and these pages are "controlled"
or centralized using a Page Controller. This not only increases readability,
but it also simplifies usage of the Page Objects.

Classes:
    - Pages

Usage:
    Each completed Page Object Model (POM) should be added
    as a property of the Pages class.

Example:
  1 def test_using_page_controller(self):
  2     pages = Pages()
  3     pages.home.goto()
  4     pages.league.goto("NA LCS")
  5     
  6     assert pages.league.map.schedule_tab.is_displayed


  1 def test_without_page_controller(self):
  2     home = HomePage(driver)
  3     home.goto()
  4     league = LeaguePage(driver)
  5     league.goto("NA LCS")
  6     
  7     assert league.map.schedule_tab.is_displayed
"""

__author__ = "Carlos Kidman"


from framework.drivercore.driver import Driver
from lol_esports.pom.home import HomePage
from lol_esports.pom.league import LeaguePage
from lol_esports.pom.teamstandings import TeamStandingsPage


class Pages:
    def __init__(self):
        self._driver = Driver("chrome")
        self._home = HomePage(self.driver)
        self._league = LeaguePage(self.driver)
        self._teamstandings = TeamStandingsPage(self.driver)

    @property
    def driver(self):
        return self._driver
    
    @property
    def home(self):
        return self._home

    @property
    def league(self):
        return self._league

    @property
    def teamstandings(self):
        return self._teamstandings
