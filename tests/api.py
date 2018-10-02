"""LOL Esports API Tests.

Run tests:
    $ pytest tests/api.py
"""


import requests
import lol_esports.data.esports as api


SUMMER_SPLIT_2018_ID = "8531db79-ade3-4294-ae4a-ef639967c393"


def test_api_get_tournament_by_guid():
    tournament = api.get_tournament_by_guid(SUMMER_SPLIT_2018_ID)
    assert tournament['title'] == "na_2018_summer"


def test_api_get_tournament_by_title():
    tournament = api.get_tournament_by_title("na_2018_summer")
    assert tournament['id'] == SUMMER_SPLIT_2018_ID


def test_api_get_team_by_slug():
    team = api.get_team_by_slug("team-liquid", SUMMER_SPLIT_2018_ID)
    assert len(team["starters"]) == 5


def test_api_get_teams():
    teams = api.get_teams(SUMMER_SPLIT_2018_ID)
    assert len(teams) > 0
