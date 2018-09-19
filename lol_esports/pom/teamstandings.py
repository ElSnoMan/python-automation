from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expect
from lol_esports.pom.pagebase import PageBase


class TeamStandingsPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self.map = TeamStandingsPageMap(driver)

    def goto(self):
        self.map.team_standings_tab.click()

    def select_stage_by_name(self, name):
        self.map.stage_dropdown.click()
        self._driver.find_element(By.XPATH, f"//a[text() = '{name.lower()}']").click()

    def select_split_by_name(self, name):
        self.map.split_dropdown.click()
        self._driver.find_element(By.XPATH, f"//a[text()='{name.lower()}']").click()


class TeamStandingsPageMap:
    def __init__(self,driver):
        self._driver = driver
    
    @property
    def team_standings_tab (self):
        return self._driver.find_element (By.XPATH, "(//a[text()='TEAMS & STANDINGS'])[last()]")
    
    @property
    def stage_dropdown (self):
        return self._driver.find_element(By.CSS_SELECTOR, "a[data-dropdown = 'drop-2']")
    
    @property
    def split_dropdown (self):
        return self._driver.find_element(By.CSS_SELECTOR, "a[data-dropdown = 'drop-1']")