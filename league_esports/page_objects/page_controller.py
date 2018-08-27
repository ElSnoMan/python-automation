from league_esports.page_objects.home import HomePage
from league_esports.page_objects.league import LeaguePage


class Pages:
    def __init__(self, driver, wait):
        self._home = HomePage(driver, wait)
        self._league = LeaguePage(driver, wait)
    
    @property
    def home(self):
        return self._home

    @property
    def league(self):
        return self._league
