from lol_esports.pom.controller import Pages
# run tests via cli using: $ pytest unit.py


def test_selenium():
    pages = Pages()
    pages.driver.goto("https://www.lolesports.com")
    pages.league.goto("NA LCS")
    assert pages.driver.title == "Schedule | LoL Esports"


def test_each_teams_standings_displayed():
    pages = Pages()
    pages.driver.goto("https://www.lolesports.com")
    pages.league.goto("NA LCS")
    pages.teamstandings.goto()
    pages.teamstandings.select_stage_by_name("Regular Season")
