from numpy.lib.function_base import _piecewise_dispatcher
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#define a class Team, which takes team name and performes the analysis
class Team():

    def __init__(self, team_name):
        self.team_name=team_name
        self.dictionary ={1: 'Overall', 2:'Home', 3:'Road', 4:'E', 5:'W',6:'A', 7:'C',8:'SE', 9:'NW', 10:'P',11:'SW', 12:'Pre' , 13:'Post', 14:'≤3', 15:'≥10', 16:'Oct', 17:'Nov', 18:'Dec', 19:'Jan', 20:'Feb', 21:'Mar', 22:'Jul', 23:'Aug'}
        self.user_input = None
        self.user_option = None
        self.data = pd.read_csv("nba_test.csv")
        self.data = self.data.fillna('1-100')
        self.team_row=self.data.loc[self.data['Team']== self.team_name]

    def win_loss_ratio(self,category):

        #get only the row of the chosen team
        category_value = self.team_row.iat[0,category]
        wins = int(category_value.split('-')[0])
        loses = int(category_value.split('-')[1])
        win_loss_ratio = round((wins / (wins+loses) *100),2)
        #print(f'The {self.dictionary[category]} win/loss ratio of {self.team_name} is {win_loss_ratio}%!')
        title = f'  Win/loss ratio in {self.dictionary[category]} category of {self.team_name}'

        return wins,loses,win_loss_ratio,title

    def monthly_win_loss(self):
        months = []
        end_range = len(self.team_row.columns)
        for i in range(16, end_range):
            month = self.win_loss_ratio(i)[2]
            months.append(month)
        return months

    def division_statistics(self):
        # creating a list of win/loss ratios for each division
        division_list = []
        for i in range(6,12):
            division_win_loss = self.win_loss_ratio(i)[2]
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
            number_games = self.win_loss_ratio(i)[0] + self.win_loss_ratio(i)[1]
            list_number_games.append(number_games)

        print("")
        print(" The highest win/loss ratio was",max(division_list),"%", f"and it was in the {name_position_max} division")
        print("")
        print(" The lowest win/loss ratio was",min(division_list),"%", f"and it was in the {name_position_min} division")
        print("")

        # looping for the 6 different divisions
        print(f" The {self.team_name} played a total of :")
        print("")
        for i in range(6):
            print('\t' * 1 + f"{list_number_games[i]} games in the {division_list_names[i]} division")
            print("")

    def conference_statistics(self):
        # creating a list of win/loss ratios for each conference
        conference_list = []
        for i in range(4,6):
            conference_win_loss = self.win_loss_ratio(i)[2]
            conference_list.append(conference_win_loss)

            # manually creating a list of the official conference names
            conference_list_names = ["East","West"]

        position_max = conference_list.index(max(conference_list))
        position_min = conference_list.index(min(conference_list))
        # fetching the corresponding conference name of the min/max win/loss ratio
        name_position_max = conference_list_names[position_max]
        name_position_min = conference_list_names[position_min]

        # creating a list of the total number of games per conference, for one team (ex:[10,8,7,15,12,9])
        list_number_games = []
        number_games = []
        for i in range(4,6):
            number_games = self.win_loss_ratio(i)[0] + self.win_loss_ratio(i)[1]
            list_number_games.append(number_games)

        print("")
        print(" The highest win/loss ratio was",max(conference_list),"%", f"and it was in the {name_position_max} conference")
        print("")
        print(" The lowest win/loss ratio was",min(conference_list),"%", f"and it was in the {name_position_min} conference")
        print("")

        # looping for the 2 different conferences
        print(f" The {self.team_name} played a total of :")
        print("")
        for i in range(2):
            print('\t' * 1 + f"{list_number_games[i]} games in the {conference_list_names[i]} conference")
            print("")

    def all_star_statistics(self):
        # creating a list of win/loss ratios for pre and post All-Star game
        all_star_list = []
        for i in range(12,14):
            all_star_win_loss = self.win_loss_ratio(i)[2]
            all_star_list.append(all_star_win_loss)

        # manually creating a list of the official all-star names
        all_star_list_names = ["Pre All-Star Game","Post All-Star Game"]

        position_max = all_star_list.index(max(all_star_list))
        position_min = all_star_list.index(min(all_star_list))
        # fetching the corresponding Division name of the min/max win/loss ratio
        name_position_max = all_star_list_names[position_max]
        name_position_min = all_star_list_names[position_min]

        # creating a list of the total number of games for pre/post all-star, for one team (ex:[10,8,7,15,12,9])
        list_number_games = []
        number_games = []
        for i in range(12,14):
            number_games = self.win_loss_ratio(i)[0] + self.win_loss_ratio(i)[1]
            list_number_games.append(number_games)

        print("")
        print(" The highest win/loss ratio was",max(all_star_list),"%", f"and it was {name_position_max}")
        print("")
        print(" The lowest win/loss ratio was",min(all_star_list),"%", f"and it was {name_position_min}")
        print("")

        # looping for the 2 different pre/post all-star
        print(f" The {self.team_name} played a total of :")
        print("")
        for i in range(2):
            print('\t' * 1 + f"{list_number_games[i]} games {all_star_list_names[i]}")
            print("")

    def game_margin_statistics(self):
        # creating a list of win/loss ratios for the game margin
        game_margin_list = []
        for i in range(14,16):
            game_margin_win_loss = self.win_loss_ratio(i)[2]
            game_margin_list.append(game_margin_win_loss)

        game_margin_list_names = ["≤3 points game margin","≥ 10 points game margin"]

        position_max = game_margin_list.index(max(game_margin_list))
        position_min = game_margin_list.index(min(game_margin_list))
        name_position_max = game_margin_list_names[position_max]
        name_position_min = game_margin_list_names[position_min]

        list_number_games = []
        number_games = []
        for i in range(14,16):
            number_games = self.win_loss_ratio(i)[0] + self.win_loss_ratio(i)[1]
            list_number_games.append(number_games)

        print("")
        print(" The highest win/loss ratio was",max(game_margin_list),"%", f"and it was in the {name_position_max} category")
        print("")
        print(" The lowest win/loss ratio was",min(game_margin_list),"%", f"and it was in the {name_position_min} category")
        print("")

        # looping for the 2 different conferences
        print(f" The {self.team_name} played a total of :")
        print("")
        for i in range(2):
            print('\t' * 1 + f"{list_number_games[i]} games with {game_margin_list_names[i]}")
            print("")

