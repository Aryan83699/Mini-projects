from fastapi import FastAPI,APIRouter
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