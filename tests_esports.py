# run tests via cli using: $ pytest unit.py --workers 2
# more info: https://docs.pytest.org/en/latest/fixture.html#fixture


import pytest
import lol_esports.data.esports as api
from framework.drivercore.driver import Driver
from lol_esports.pom.controller import Pages


@pytest.fixture
def setup():
    driver = Driver("chrome")
    pages = Pages(driver)
    yield driver, pages
    driver.quit()


def test_esports_pom(setup):
    driver, pages = setup
    driver.goto("https://www.lolesports.com")
    pages.league.goto("NA LCS")
    assert driver.title == "Schedule | LoL Esports"


def test_each_teams_standings_displayed(setup):
    driver, pages = setup
    driver.goto("https://www.lolesports.com")
    pages.league.goto("NA LCS")
    pages.teamstandings.goto()
    pages.teamstandings.select_stage_by_name("Regular Season")
    
    for api_team in pages.teamstandings.get_teams_from_api():
        team = pages.teamstandings.find_regseason_team(api_team["name"])
        assert team.is_displayed
