from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expect
from lol_esports.pom.pagebase import PageBase
from lol_esports.data import esports as api


class TeamStandingsPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self.map = TeamStandingsPageMap(driver)

    def goto(self):
        self.map.team_standings_tab.click()

    def find_regseason_team(self, name):
        """Get team from the Regular Season view.
        
        Returns:
            Team Row (Element) that contains the name.
        """
        return next(row for row in self.map.regseason_team_rows if name in row.text)

    def get_teams_from_api(self):
        """Gets a list of Team objects from the Teams API.
        
        Returns:
            Currently only returns the teams from '2018-summer-split'.
        """
        guid = api.tournament_guids['2018-summer-split']
        rosters = api.get_tournament_by_guid(guid)['rosters']
        all_teams = api.get_teams(guid)
        teams = []
        for key in rosters:
            id = rosters[key]['team']
            team = next(t for t in all_teams if t['id'] == int(id))
            teams.append(team)
        return teams

    def select_stage_by_name(self, name):
        """Selects the Stage from the Stage dropdown."""
        self.map.stage_dropdown.click()
        self._driver.find_element(By.XPATH, f"//a[text() = '{name.lower()}']").click()

    def select_split_by_name(self, name):
        """Selects the Split from the Split dropdown."""
        self.map.split_dropdown.click()
        self._driver.find_element(By.XPATH, f"//a[text()='{name.lower()}']").click()


class TeamStandingsPageMap:
    def __init__(self, driver):
        self._driver = driver
    
    @property
    def team_standings_tab (self):
        return self._driver.find_element(By.XPATH, "(//a[text()='TEAMS & STANDINGS'])[last()]")

    @property
    def regseason_team_rows(self):
        return self._driver.find_elements(By.CSS_SELECTOR, ".team-row")
    
    @property
    def stage_dropdown (self):
        return self._driver.find_element(By.CSS_SELECTOR, "a[data-dropdown = 'drop-2']")
    
    @property
    def split_dropdown (self):
        return self._driver.find_element(By.CSS_SELECTOR, "a[data-dropdown = 'drop-1']")
