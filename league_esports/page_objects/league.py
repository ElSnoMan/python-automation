from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expect


class LeaguePage:
    def __init__(self, driver, wait):
        self._driver = driver
        self._wait = wait
        self.map = LeaguePageMap(driver)

    def goto(self):
        self.map.nalcs_tab.click()
        self.wait_for_page_load()

    def wait_for_page_load(self):
        self._wait.until(expect.element_to_be_clickable(
            self.map.schedule_tab.locator))


class LeaguePageMap:
    def __init__(self, driver):
        self._driver = driver

    @property
    def nalcs_tab(self):
        tabs = self._driver.find_elements(
            By.XPATH, "//ul[@class='main-nav-menu']/li/a")
        # .First() equivalent
        return next(tab for tab in tabs if "NA LCS" in tab.text)

    @property
    def league_nav_container(self):
        return self._driver.find_element(By.CSS_SELECTOR, ".league-nav-container")

    @property
    def schedule_tab(self):
        return self._driver.find_element(By.XPATH, "(//a[@href='/en_US/na-lcs/na_2018_summer/schedule'])[2]")

    @property
    def schedule_container(self):
        return self._driver.find_element(By.ID, "schedule")
