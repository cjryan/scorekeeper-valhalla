import xml.etree.ElementTree as ET
import MySQLdb
import urllib2
from datetime import date
from calendar import monthrange

# Connect to the database
#db = MySQLdb.connect(host="", user="", passwd="", db="")

# Create a database cursor to manipulate the data
#cursor = db.cursor()


def printscores(url, month, day):
	#Read in the XML file so that python can parse it
	tree = ET.parse(urllib2.urlopen(url))

	#Find the top level element in the XML file
	games = tree.getroot()

	#Find the interleague games using the 'league' attribute. in the "AN"
	#or "NA" construct, the away team is first. 
	for game in games:		

		#game tag attributes
		home_team_name = game.get('home_team_name')
		away_team_name = game.get('away_team_name')
		league = game.get('league')
	
		league_position =  league.find("A")
		if league_position == 0:
			away_team_league = "AL"
			home_team_league = "NL"
		elif league_position == 1:
			home_team_league = "AL"
			away_team_league = "NL"

		#game tag children elements
		for linescore in game.findall('linescore'):
			final_runs = linescore.find('r')
			home_final_runs = final_runs.get('home')
			away_final_runs = final_runs.get('away')

			#print home_final_runs, away_final_runs	

			if league == "AN":
				print str(month) + " " + str(day) + "\n"
				print "Interleague: " + league + " \n" + away_team_name + " " + away_team_league + " Score: " + away_final_runs + "\n" + home_team_name + " " + home_team_league + " Score: " + home_final_runs + "\n"
				#cursor.execute("""INSERT INTO interleague_score_comp (al_team, al_team_score, nl_team, nl_team_score) VALUES (%s, %s, %s, %s)""", (away_team_name, away_final_runs, home_team_name, home_final_runs))
			elif league == "NA":
				print str(month) + " " + str(day) + "\n"
				print "Interleague: " + league + " \n" + away_team_name + " " + away_team_league + " Score: " + away_final_runs + "\n" + home_team_name + " " + home_team_league + " Score: " + home_final_runs + "\n"
				#cursor.execute("""INSERT INTO interleague_score_comp (nl_team, nl_team_score, al_team, al_team_score) VALUES (%s, %s, %s, %s)""", (away_team_name, away_final_runs, home_team_name, home_final_runs))


#Pull down all the master_scoreboard.xml files. This will be in the structure of:
#http://gd2.mlb.com/components/game/mlb/year_2013/month_01/day_01/

current_year = date.today().year
print current_year

#Get the months, and add a leading zero if less than 10 to conform with the mlb url structure. 

for month in range(1,13):
	#monthrange supports leapyear, too.
	day_range = monthrange(current_year, month)
	#for the range function below to include the last day of the month
	day_range = day_range[1] + 1 
	#print day_range

	for day in range(1, day_range):
		if day < 10:
			day = "0" + str(day)

	        if month < 10:
        	        month_zero = "0" + str(month)
	
			mlb_url = "http://gd2.mlb.com/components/game/mlb/year_2013/month_%s/day_%s/master_scoreboard.xml" % (month_zero, day)

			printscores(mlb_url, month_zero, day)
			#print month_zero, day
		else:
        	        mlb_url = "http://gd2.mlb.com/components/game/mlb/year_2013/month_%s/day_%s/master_scoreboard.xml" % (month, day)

        	        printscores(mlb_url, month, day)
			#print month, day
	
