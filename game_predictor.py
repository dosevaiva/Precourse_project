import pandas as pd
from  team_analysis import *
 
class GamePredictor():
    def __init__(self):
        #data = pd.read_csv("nba_test.csv")
        self.team=Team()
        self.game=input('Where does the first team play? \n 1. Home \n 2. Road \n ')
        self.opp_team = input("Enter the opposing team: ").title()

        self.team.data['Wins']=pd.to_numeric(self.team.data.Overall.str.split('-',expand=True)[0])
        self.team.data['Loses']=pd.to_numeric(self.team.data.Overall.str.split('-',expand=True)[1])
        self.team.data['Home_Wins']=pd.to_numeric(self.team.data.Home.str.split('-',expand=True)[0])
        self.team.data['Home_Loses']=pd.to_numeric(self.team.data.Home.str.split('-',expand=True)[1])
        self.team.data['Road_Wins']=pd.to_numeric(self.team.data.Road.str.split('-',expand=True)[0])
        self.team.data['Road_Loses']=pd.to_numeric(self.team.data.Road.str.split('-',expand=True)[1])

        self.team.data['Total']=self.team.data['Wins']+self.team.data['Loses']
        self.team.data['Success Ratio']=round(self.team.data['Wins']/self.team.data['Total'],3)
        self.team.data['Home_Total']=self.team.data['Wins']+self.team.data['Loses']
        self.team.data['Home Success Ratio']=round(self.team.data['Home_Wins']/self.team.data['Home_Total'],3)
        self.team.data['Home Loses Ratio']=round(self.team.data['Home_Loses']/self.team.data['Home_Total'],3)
        self.team.data['Road_Total']=self.team.data['Road_Wins']+self.team.data['Road_Loses']
        self.team.data['Road Success Ratio']=round(self.team.data['Road_Wins']/self.team.data['Road_Total'],3)
        self.team.data['Road Loses Ratio']=round(self.team.data['Road_Loses']/self.team.data['Road_Total'],3)

        self.team_data = (self.team.data[self.team.data.Team == self.team.team_name])
        #print(self.team_data)
        self.opp_team_data = (self.team.data[self.team.data.Team == self.opp_team])
        print(self.opp_team_data)
        self.c = 0
        #quit()
        #data = pd.read_csv("nba_test.csv"

    def predict(self):

        if self.game == '1':
            self.c = (self.team_data['Home Success Ratio'].values + self.opp_team_data['Road Loses Ratio'].values) - (self.team_data['Home Success Ratio'].values * self.opp_team_data['Road Loses Ratio'].values)
                # print(team_name, c)
            
        elif self.game == '2':
            self.c = (self.team_data['Road Success Ratio'].values + self.opp_team_data['Home Loses Ratio'].values) - (self.team_data['Road Success Ratio'].values * self.opp_team_data['Home Loses Ratio'].values)
            
        print(f'{self.team.team_name} will win with probability  {self.c*100} %')

      
