from numpy.lib.function_base import _piecewise_dispatcher
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#define a class Team, which takes team name and performes the analysis
class Team():

    def __init__(self):

        while True:
            self.team_name = input("Team name: ").title()
            self.data = pd.read_csv("nba_test.csv")
            self.data = self.data.fillna('1-100')
            self.team_row=self.data.loc[self.data['Team']== self.team_name]

            print(self.team_row)

            if len(self.team_row) == 0:
                print('This is not a valid team name!')
                continue
            else:
                break

        self.dictionary ={1: 'Overall', 2:'Home', 3:'Road', 4:'E', 5:'W',6:'A', 7:'C',8:'SE', 9:'NW', 10:'P',11:'SW', 12:'Pre' , 13:'Post', 14:'≤3', 15:'≥10', 16:'Oct', 17:'Nov', 18:'Dec', 19:'Jan', 20:'Feb', 21:'Mar', 22:'Jul', 23:'Aug'}
        self.user_input = None
        self.user_option = None
        self.data_visual = ShowData()

    def win_loss_ratio(self,category):

        #get only the row of the chosen team
        category_value = self.team_row.iat[0,category]
        wins = int(category_value.split('-')[0])
        loses = int(category_value.split('-')[1])
        win_loss_ratio = round((wins / (wins+loses) *100),2)
        #print(f'The {self.dictionary[category]} win/loss ratio of {self.team_name} is {win_loss_ratio}%!')
        title = f'  Win/loss ratio in {self.dictionary[category]} category of {self.team_name}'

        # return wins and losses
        return wins,loses,win_loss_ratio,title

    def monthly_win_loss(self):
        months = []
        for i in range(16,24):
            month = self.win_loss_ratio(i)[2]
            months.append(month)
        return months

    def divison_comparison(self):
        # creating a list of win/loss ratios for each division
        division_list = []
        for i in range(6,12):
            division_win_loss = self.win_loss_ratio(i,False)[2]
            division_list.append(division_win_loss)

        # manually creating a list of the official division names
        division_list_names = ["Atlantic","Central","South-East","North-West","Pacific","South-West"]

        position_max = division_list.index(max(division_list))
        position_min = division_list.index(min(division_list))
        # fetching the corresponding Division name of the min/max win/loss ratio
        name_position_max = division_list_names[position_max]
        name_position_min = division_list_names[position_min]

        # creating a list of the total number of games per division, for one team (ex:[10,8,7,15,12,9])
        list_number_games = []
        number_games = []
        for i in range(6,12):
            number_games = self.win_loss_ratio(i,False)[0] + self.win_loss_ratio(i,False)[1]
            list_number_games.append(number_games)

        print("")
        print("The highest win/loss ratio was",max(division_list),"%", f"and it was in the {name_position_max} division")
        print("")
        print("The lowest win/loss ratio was",min(division_list),"%", f"and it was in the {name_position_min} division")
        print("")

        # looping for the 6 different divisions
        print(f"The {team_name} played a total of :")
        print("")
        for i in range(6):
            print('\t' * 1 + f"{list_number_games[i]} games in the {division_list_names[i]} division")
            print("")

            
class ShowData():

    #Define a function to create a piechart based on wins and losses in any category
    def piechart_win_loss_ratio(self, wins ,loses,title):
        labels = 'Wins', 'Losses'
        sizes = [wins,loses]
        explode = (0.1 ,0)
        colors = ['#e38d8d', '#95b7ed']

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',startangle=90, colors=colors)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.set_title(title)
        plt.savefig('plots.png')

    def linechart(self,y):
        x = np.linspace(1,100,8)
        x_text = ['Oct', 'Nov','Dec','Jan','Feb','Mar','Jul','Aug']
        plt.figure()
        plt.title('Monthly performance graph')
        plt.ylabel('%')
        plt.xticks(x,x_text)
        plt.plot(x,y)
        plt.savefig('plots.png')
