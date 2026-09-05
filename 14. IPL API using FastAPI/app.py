from fastapi import FastAPI,APIRouter,Query,HTTPException
from typing import Annotated
import api



app=FastAPI(title="IPL API",description="This backend provides the anlaytical APIs of the IPL datasets")

teams=APIRouter(prefix='/teams')
app.include_router(teams)

@app.get('/')
def home():
    return {"IPL API"}

@teams.get('/names')
def names():
    return api.get_teams()

@teams.get('/teamVteam')
def teamVsteam(team1:Annotated[str,Query(title="Team Name")],team2:Annotated[str,Query(title="Team Name")]):

    data=api.teamVteam(team1,team2)
    if data.get('Total Matches')==0:
        raise HTTPException(status_code=404,detail="No Match or No Data related to team")
    return data

@teams.get('/teams-record')
def teams_record(team:Annotated[str,Query(title="Team Name")]):
    data=api.team_record(team)
    if not data:
        raise HTTPException(status_code=404,detail="No Match or No Data related to team")
    return data



@teams.get('/teams-overall')
def team_overall(team:Annotated[str,Query(title="Team Name")]):
    data=api.team_overall(team)
    return data