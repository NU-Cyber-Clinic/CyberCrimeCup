import requests
from bs4 import BeautifulSoup
from operator import itemgetter

teamScores = {}
playerScores = {}
cookies = {"PHPSESSID": "CHANGE_ME"}
challengeIds = (101, 102, 103, 104, 105, 106, 107, 108, 109, 201)

## Get team and player data
for challenge in challengeIds:
	url = "https://www.cybercrime.co.uk/dashboard-challenge-preview/" + str(challenge)

	response = requests.request("GET", url, cookies=cookies)

	# html5lib needed for formatting as the page is really bad and not valid html
	# pip install html5lib
	page = BeautifulSoup(response.text, features="html5lib")

	tables = page.find_all("div", {"class": "table-responsive-xl"})

	for row in tables[0].table.tbody.find_all("tr"):
		rowParts = row.find_all("td")
		if (len(rowParts) >= 1 and not ("colspan" in rowParts[0].attrs)):
			point = int((rowParts[0].get_text().replace("Pts", "")))
			team = rowParts[1].get_text()
			uni = rowParts[2].get_text()
			if (team in teamScores):
				teamInfo = list(teamScores[team])
				teamInfo[0] += point
				teamScores[team] = tuple(teamInfo)
			else:
				teamScores[team] = (point, uni)
	
	for row in tables[1].table.tbody.find_all("tr"):
		rowParts = row.find_all("td")
		if (len(rowParts) >= 1 and not ("colspan" in rowParts[0].attrs)):
			point = int((rowParts[0].get_text().replace("Pts", "")))
			player = rowParts[1].get_text()
			team = rowParts[2].get_text()
			uni = rowParts[3].get_text()
			if (player in playerScores):
				playerInfo = list(playerScores[player])
				playerInfo[0] += point
				playerScores[player] = tuple(playerInfo)
			else:
				playerScores[player] = (point, team, uni)

## Sort arrays
teamScores = sorted(teamScores.items(), key=itemgetter(1), reverse=True)
playerScores = sorted(playerScores.items(), key=itemgetter(1), reverse=True)

## Put teams in csv
with open("teams.csv", 'w') as f:
	for teamData in teamScores:
		teamName = teamData[0]
		teamInfo = teamData[1]
		f.write(str(teamInfo[0]) + "," + teamName + "," + teamInfo[1] + "\n")

## Put players in csv
with open("players.csv", 'w') as f:
	for playerData in playerScores:
		playerName = playerData[0]
		playerInfo = playerData[1]
		f.write(str(playerInfo[0]) + "," + playerName + "," + playerInfo[1] + "," + playerInfo[2] + "\n")