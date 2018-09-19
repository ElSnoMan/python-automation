"""Classes and functionalities that are shared across all pages on lolesports.

There are three sections that each page shares:
    - Riot Navbar: Navigates to other websites (top-most menu with gold text)
    - Main Navbar: Navigates to other pages within website (under Riot Menu)
    - Footer: terms of use, privacy policy, social links, etc.

Classes:
    - PageBase
    - PageBaseMap

Usage:
    Each Page Object should inherit from a Page Base.

Example:
  1 class HomePage(PageBase):
  2     def __init__(self, driver, wait):
  3         super().__init__(driver, wait)
  4
  5     def goto(self):
  6         self.goto_home()
  7         # rest of class

    Line 1: HomePage inherits PageBase.
    Line 3: Call super() to run __init__ from PageBase.
    Line 6: You can now call self.goto_home() method directly in HomePage.
"""

__author__ = "Carlos Kidman"

from selenium.webdriver.common.by import By


class PageBase:
    """Base class to share functionality and elements across all pages."""

    def __init__(self, driver):
        self._driver = driver
        self.basemap = PageBaseMap(driver)

    def select_locale(self, region_abbr, language):
        """Selects the localization for the website.

        This action will take the user to the lolesports.com version
        of the appropriate localization. Different versions have different
        element maps.

        NOTE:
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
        """Go to the specified League's page.
        
        Args:
            - league (str): the name of the League.

        Example:
            - goto_league("NA LCS")
            - goto_league("World Championship")
        """
        self.basemap.main_navbar_tab(league).click()

    def goto_tickets(self):
        self.basemap.main_navbar_tab("Tickets").click()

    # Riot Websites Navigation
    def goto_universe(self):
        self.basemap.riot_navbar_tab("universe").click()


class PageBaseMap:
    """Base element map to share common elements across all pages.
    
    NOTE:
        Do not instantiate this class directly in tests.
        Access this element map through the self.basemap property in PageBase.
    """
    def __init__(self, driver):
        self._driver = driver

    def riot_navbar_tab(self, tabname):
        """Get the Riot Navbar tab by name.

        NOTE:
            Since the link-id of the tab is all lowercase,
            we can simply call the .lower() function.
            This means that tabname is not case-sensitive.

        Args:
            - tabname (str): the name of the tab as shown on the website.

        Examples:
            - news_tab = riot_navbar_tab("NEWS")
            - universe_tab = riot_navbar_tab("universe")
        """
        return self._driver.find_element(By.CSS_SELECTOR,
            f".riotbar-navbar-link[data-riotbar-link-id='{tabname.lower()}']")

    def main_navbar_tab(self, tabname):
        """Get the Main Navbar tab by name.

        NOTE:
            - tabname is case-sensitive
            - Not all tab names are uppercase

            To validate the tab name, inspect the tab
            in the DOM and copy its text.

        Args:
            - tabname (str): the name of the tab as shown in the DOM.

        Examples:
            - home_tab = main_navbar_tab("HOME")
            - tickets_tab = main_navbar_tab("Tickets")
        """
        return self._driver.find_element(By.XPATH,
            f"//ul[@class='main-nav-menu']/li/a[text()='{tabname}']")

    def current_locale_button(self):
        return self._driver.find_element(By.ID, "riotbar-locale-switch-trigger")

    def region_dropdown(self):
        return self._driver.find_element(By.ID, "riotbar-region-dropdown-trigger")

    def region_option(self, region_abbr):
        """Get the Region Option by the region's abbreviation.

        NOTE:
            - tabname is not case-sensitive
            
            To validate the tab name, inspect the region option
            in the DOM and copy its region-id.

        Args:
            - region_abbr (str): the region abbreviaton as shown in the DOM.

        Examples:
            - north_america_option = region_option("na")
            - eu_nordic_and_east = region_option("eune")
        """
        return self._driver.find_element(By.ID, f"riotbar-region-option-{region_abbr.lower()}")

    def region_language(self, region_abbr, language):
        """Get the Region Language by the region's abbreviation and language.

        NOTE:
            - region_abbr is not case-sensitive
            - language is case-sensitive

            To validate these values, inspect the language option
            in the DOM and copy its region-id and text.

        Args:
            - region_abbr (str): the region abbreviaton as shown in the DOM.
            - language (str): the language as shown in the DOM or website

        Examples:
            - north_america_english = region_language("na", "English")
            - eu_nordic_and_east_polski = region_language("eune", "Polski")
        """
        return self._driver.find_element(By.XPATH,
            f"//div[@id='riotbar-languages-{region_abbr.lower()}'] \
            //a[contains(text()='{language}')]")
