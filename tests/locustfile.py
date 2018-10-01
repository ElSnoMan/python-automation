"""Performance Testing with Locust

Things we measure:
- Availability or Uptime
- Concurrency
- Throughput
- Response Time
- Network Utilization
- Server Utilization

Sample Data
------------
framework -> lol_esports -> data
There are request_stats and response_time .csv files
* 1000 users max
* hatch 10 users per second
* ran for 60 seconds

Usage
------
1. Run the locust service and load the specified locust file
$ locust -f tests/locustfile.py --host=https://lolesports.com

2. Go to http://127.0.0.1:8089/ and start the run
"""


from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    """Set of tasks to be run my each user"""
    # def on_start(self):
    #     """ on_start is called when a Locust starts, before any task is scheduled."""
    #     self.login()

    # def on_stop(self):
    #     """ on_stop is called when the TaskSet is stopping."""
    #     self.client.post("/logout")

    # def login(self):
    #     self.client.post('/login', {'username': 'foo', 'password': 'bar'})

    @task(1)
    def news(self):
        self.client.get('https://na.leagueoflegends.com/en/news/', name='news')

    @task(1)
    def game(self):
        self.client.get('https://na.leagueoflegends.com/en/game-info/', name='game')

    @task(1)
    def universe(self):
        self.client.get('https://universe.leagueoflegends.com/en_US/', name='universe')

    @task(1)
    def nexus(self):
        self.client.get('https://nexus.leagueoflegends.com/en-us/', name='nexus')

    @task(1)
    def community(self):
        self.client.get('https://boards.na.leagueoflegends.com/en/', name='community')

    @task(1)
    def support(self):
        self.client.get('https://support.riotgames.com/hc/en-us', name='support')

    @task(1)
    def merch(self):
        self.client.get('https://na.merch.riotgames.com/en/', name='merch')


class WebsiteUser(HttpLocust):
    """The user"""
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
