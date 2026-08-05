record = int(input())
team_score = {}
teamCount = 0

for i in range(record):
	team, score = input().split()
	
	if team in team_score:
		team_score[team] += int(score)
	else:
		team_score[team] = int(score)
		teamCount += 1

for key, value in team_score.items():
	print(key, value)