import requests


API_URL = "https://api.lolesports.com/api/v1"


### leagues api ###
def get_tournament_by_guid(guid):
    response = leagues_api_response("na-lcs")
    return next(t for t in response["highlanderTournaments"] if t["id"] == guid)


def get_tournament_by_title(title):
    response = leagues_api_response("na-lcs")
    return next(t for t in response["highlanderTournaments"] if t["title"] == title)


def leagues_api_response(slug):
    return requests.get(f"{API_URL}/leagues?slug={slug}").json()


### teams api ###
def get_teams(tournament_guid):
    response = teams_api_response("team-liquid", tournament_guid)
    return response["teams"]


def get_team_by_id(id, slug, tournament_guid):
    response = teams_api_response(slug, tournament_guid)
    return next(t for t in response["teams"] if t["id"] == id)


def get_team_by_slug(slug, tournament_guid):
    response = teams_api_response(slug, tournament_guid)
    return next(t for t in response["teams"] if t["slug"] == slug)


def get_team_by_guid(guid, slug, tournament_guid):
    response = teams_api_response(slug, tournament_guid)
    return next(t for t in response["teams"] if t["guid"] == guid)


def teams_api_response(slug, tournament_guid):
    return requests.get(f"{API_URL}/teams?slug={slug}&tournament={tournament_guid}").json()


## IDs ##
league_guids = {
    "na-lcs": "3496bcf8-d7b5-11e6-84c1-06bf49dcca99"
}

tournament_guids = {
    "2018-summer-split": "8531db79-ade3-4294-ae4a-ef639967c393"
}
