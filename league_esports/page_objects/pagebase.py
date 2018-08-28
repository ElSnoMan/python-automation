from selenium.webdriver.common.by import By


class PageBase:
    def __init__(self, driver, wait):
        self._driver = driver
        self._wait = wait
        self.basemap = PageBaseMap(driver)

    def select_locale(self, region_abbr, language):
        """Selects the localization for the website. \n
        This action will take the user to the lolesports.com version
        of the appropriate localization. Different versions have different
        element maps.

        Note:
            - params are case-sensitive

        Args:
            - region_abbr (str): abbreviation for the region.
            - language (str): preferred language for the above region.

        Examples:
            - select_locale("na", "English")
            - select_locale("eune", "Polski")
        """
        self.basemap.current_locale_button().click()
        self.basemap.region_dropdown().click()
        self.basemap.region_option(region_abbr).click()
        self.basemap.region_language(region_abbr, language).click()

    # eSports Page Navigation
    def goto_home(self):
        self.basemap.main_navbar_tab("HOME").click()

    def goto_league(self, league):
        self.basemap.main_navbar_tab(league).click()

    def goto_tickets(self):
        self.basemap.main_navbar_tab("Tickets").click()

    # Riot Websites Navigation
    def goto_universe(self):
        self.basemap.riot_navbar_tab("universe").click()


class PageBaseMap:
    def __init__(self, driver):
        self._driver = driver

    def riot_navbar_tab(self, tabname):
        return self._driver.find_element(By.CSS_SELECTOR,
            f".riotbar-navbar-link[data-riotbar-link-id='{tabname.lower()}']")

    def main_navbar_tab(self, tabname):
        return self._driver.find_element(By.XPATH,
            f"//ul[@class='main-nav-menu']/li/a[text()='{tabname}']")

    def current_locale_button(self):
        return self._driver.find_element(By.ID, "riotbar-locale-switch-trigger")

    def region_dropdown(self):
        return self._driver.find_element(By.ID, "riotbar-region-dropdown-trigger")

    def region_option(self, region_abbr):
        return self._driver.find_element(By.ID, f"riotbar-region-option-{region_abbr}")

    def region_language(self, region_abbr, language):
        return self._driver.find_element(By.XPATH,
            f"//div[@id='riotbar-languages-{region_abbr}']//a[contains(text()='{language}')]")
