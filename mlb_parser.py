import xml.etree.ElementTree as ET

#Read in the XML file so that python can parse it
tree = ET.parse('master_scoreboard.xml')

#Find the top level element in the XML file
games = tree.getroot()

#Find the interleague games using the 'league' attribute. in the "AN"
#or "NA" construct, the away team is first. 
for game in games:

	#game tag attributes
	home_team_name = game.get('home_team_name')
	away_team_name = game.get('away_team_name')
	league = game.get('league')

	#game tag children elements
	for linescore in game.findall('linescore'):
		final_runs = linescore.find('r')
		home_final_runs = final_runs.get('home')
		away_final_runs = final_runs.get('away')

		#print home_final_runs, away_final_runs
	
		if (league == "AN") or (league == "NA"):
			print "Interleague: " + league + " \n" + away_team_name + " Score: " + away_final_runs + "\n" + home_team_name + " Score: " + home_final_runs + "\n"	
