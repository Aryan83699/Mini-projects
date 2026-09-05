import pandas as pd
import numpy as np


matches=pd.read_csv("matches.csv")

# preprocessing on the data for faster operation 
matches=matches.dropna()  # removing null values 
matches["id"]=matches["id"].astype('int8')                      #converting to smaller dtypes 
matches['dl_applied']=matches['dl_applied'].astype('int8')
matches['win_by_runs']=matches['win_by_runs'].astype('int8')
matches['win_by_wickets']=matches['win_by_wickets'].astype('int16')


balls=pd.read_csv("balls.csv")

#preprocessing for faster operation 
balls["ID"]=balls["ID"].astype("int32")
balls["innings"]=balls["innings"].astype("int8")
balls["overs"]=balls["overs"].astype("int8")
balls["ballnumber"]=balls["ballnumber"].astype("int8")
balls["batsman_run"]=balls["batsman_run"].astype("int8")
balls["total_run"]=balls["total_run"].astype("int8")
balls["extras_run"]=balls["extras_run"].astype("int8")
balls["non_boundary"]=balls["non_boundary"].astype("category")
balls["isWicketDelivery"]=balls["isWicketDelivery"].astype("category")
balls["extra_type"]=balls["extra_type"].astype("category")





def get_teams():
    teams=np.append(matches.team1,matches.team2)
    total_teams=np.unique(teams)
    return {"total teams":len(total_teams),"teams":total_teams.tolist()}



def teamVteam(team1:str,team2:str):
    temp_matches=matches[((matches['team1']==team1) & (matches['team2']==team2)) | ((matches['team1']==team2) & (matches['team2']==team1))]
    total_matches=matches.shape[0]
    team1Wins=matches[matches['winner']==team1].shape[0]
    team2Wins=matches[matches['winner']==team2].shape[0]
    total_draws=total_matches-(team1Wins+team2Wins)
    seasons=matches['season'].unique().tolist()
    toss_win_t1 = (matches['toss_winner'] == team1).sum()
    toss_win_t2 = (matches['toss_winner'] == team2).sum()

    
    return {"Team1":team1 , "Team2": team2, "Total Matches":total_matches, "Total Team1 Wins":team1Wins, "Total Team2 Wins":team2Wins,      "Draws":total_draws ,"Toss Wins Team1":int(toss_win_t1),"Toss Wins Team2":int(toss_win_t2),"Seasons":seasons}



def team_record(team:str):
    temp_matches=matches[(matches['team1']==team) | (matches['team2']==team)].copy()
    matches_played=temp_matches.shape[0],
    wins=temp_matches[(temp_matches['winner']==team) & (temp_matches['result']=='normal')].shape[0]
    loss=temp_matches[~(temp_matches['winner']==team) & (temp_matches['result']=='normal')].shape[0]
    noResult=temp_matches[temp_matches['result'].isin(['no result','tie'])].shape[0]
    return {
        "Total Matches":matches_played,
        "Total Wins":wins,
        "Total Loss":loss,
        "Tie":noResult
    }




def team_overall(team:str):
    temp_matches=matches[(matches['team1']==team) | (matches['team2']==team)].copy()
    temp_data=team_record(team)
    unique_teams=matches.team1.unique()
    against={team2:teamVteam(team,team2) for team2 in unique_teams}

    return {
        "Overall Record":temp_data,
        "Against Record":against
    }

