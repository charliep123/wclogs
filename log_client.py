import requests
from report import ReportInfo


api_key = "3ad198f1b6979ef5a1f98c6af0706914"

class LogClient:
    def __init__(self, url: str, api_key: str):
        """Creates a client for accessing the warcraft log api
        """
        self.url = url
        self.params = {"api_key": api_key}

    def classes(self):
        url = f"{self.url}/classes"
        json = requests.get(url, params=self.params).json()
        return json

    def reports(self, guild_name: str, server_name: str):
        url = f"{self.url}/reports/guild/{guild_name}/{server_name}/US"
        json = requests.get(url, params=self.params).json()
        return [ReportInfo(**i) for i in json]

    def fight(self, code: str):
        url = f"{self.url}/report/fights/{code}"
        json = requests.get(url, params=self.params).json()
        return json

    def debuffs(self, fight_code):
        url = f"{self.url}/report/events/debuffs/{fight_code}"
        print(url)
        params = self.params
        params["start"] = 6599000
#        params["start"] = 6373055
        params["end"] =  6599782
        params["hostility"] = 1
        json = requests.get(url, params=params).json()
        return json


client = LogClient("https://classic.warcraftlogs.com:443/v1", api_key)
#print(client.reports(guild_name="PRIMORDIAL", server_name="Kirtonos"))
fights = client.fight("w3BgN7ZTQfmH6hXt")["fights"]
#print(fights)
for fight in fights:
    if fight["boss"] != 0:
        print(fight)
#print(client.fight("w3BgN7ZTQfmH6hXt")["fights"])
debuffs = client.debuffs("w3BgN7ZTQfmH6hXt")
print(debuffs)
#for debuf in debuffs:
#    print(debuf)
