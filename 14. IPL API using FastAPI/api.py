import pandas as pd
import numpy as np


df=pd.read_csv("matches.csv")

# droping the null values which are less than 1% of total.
df=df.dropna()

def get_teams():
    teams=np.append(df.team1,df.team2)
    total_teams=np.unique(teams)
    return {"total teams":len(total_teams),"teams":total_teams.tolist()}



def teamVteam(team1:str,team2:str):
    matches=df[((df['team1']==team1) & (df['team2']==team2)) | ((df['team1']==team2) & (df['team2']==team1))]
    total_matches=matches.shape[0]
    team1Wins=matches[matches['winner']==team1].shape[0]
    team2Wins=matches[matches['winner']==team2].shape[0]
    total_draws=total_matches-(team1Wins+team2Wins)
    seasons=matches['season'].unique().tolist()
    toss_win_t1=matches['toss_winner'].value_counts()[team1]
    toss_win_t2=matches['toss_winner'].value_counts()[team2]
    print(toss_win_t2)

    return {"Team1":team1 , "Team2": team2, "Total Matches":total_matches, "Total Team1 Wins":team1Wins, "Total Team2 Wins":team2Wins,      "Draws":total_draws ,"Toss Wins Team1":int(toss_win_t1),"Toss Wins Team2":int(toss_win_t2),"Seasons":seasons}

