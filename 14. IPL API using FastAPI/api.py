import pandas as pd
import numpy as np


matches=pd.read_csv("matches.csv")



def get_teams():
    teams=np.append(matches.team1,matches.team2)
    total_teams=np.unique(teams)
    return {"total teams":len(total_teams),"teams":total_teams.tolist()}


print(get_teams())