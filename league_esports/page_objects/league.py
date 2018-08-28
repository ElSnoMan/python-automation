from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expect
from league_esports.page_objects.pagebase import PageBase


class LeaguePage(PageBase):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self._driver = driver
        self._wait = wait
        self.map = LeaguePageMap(driver)

    def goto(self, league):
        self.goto_league(league)
        self.wait_for_page_load()

    def wait_for_page_load(self):
        self._wait.until(expect.element_to_be_clickable(
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
