from game_predictor import GamePredictor
from team_analysis import *
import time

class Menu():

    def __init__(self):
        #put this is menu
        while True:
            self.team_name = input("\n Please enter the official name of an NBA team OR press 'T' to show all teamnames: ").title()
            print("-----------------------------------------------------------------------------------------")
            self.user_team = Team(self.team_name)
            #print(self.team_row)
            if self.team_name =='T':
                self.print_team_names()

            elif len(self.user_team.team_row) == 0:
                print(' This is not a valid team name!')
                continue

            else:
                break

    def print_team_names(self):

        teams = []
        for i in range (len(self.user_team.data.index)):
            value = self.user_team.data.iat[i,0]
            teams.append(value)
        print('')
        print('/ '.join(teams))
        print('')

    def user_menu(self):
        while True:
            print('\n What metric do you want to see? \n\n 1. Win/loss ratio \n 2. Overall statistics \n 3. Monthly graph \n\n OR enter 4 if you want to access the Game Result Predictor \n\n OR type Q to quit \n')
            user_option_main_menu = input(" Enter here the number corresponding to your choice: ").lower()
            time.sleep(2)

            if user_option_main_menu == '1':
                print('\n Which win ratio do you want to see? \n\n 1. Overall \n 2. Home \n 3. Road \n\n OR press any button to go back to the main menu!\n')
                user_option_sub_menu=input(' Input a number between 1 and 3: ')
                try:
                    user_option_sub_menu = int(user_option_sub_menu)
                    if user_option_sub_menu < 1 or user_option_sub_menu > 3:
                        print(' This is not a valid option!')
                        time.sleep(1)
                    else:
                        a = self.user_team.win_loss_ratio(user_option_sub_menu)
                        self.user_team.data_visual.piechart_win_loss_ratio(a[0], a[1], a[3])
                        print("\n -> See graph in plots.png \n ")
                        print("-----------------------------------------------------------------------------------------")
                        time.sleep(1)
                except (TypeError, ValueError) as e:
                    print(' Not a valid option. Choose again')
                    continue

            elif user_option_main_menu == '2':
                print("\n What category of statistics do you want to see? \n\n 1. Conference \n 2. Division \n 3. All-Star \n 4. Game margin \n")
                user_option_sub_menu = input(' Input a number between 1 and 4: ')
                print('')
                try:
                    if user_option_sub_menu == '1':
                        self.user_team.conference_statistics()
                        print("-----------------------------------------------------------------------------------------")
                        time.sleep(1)
                    elif user_option_sub_menu == '2':
                        self.user_team.division_statistics()
                        print("-----------------------------------------------------------------------------------------")
                        time.sleep(1)
                    elif user_option_sub_menu == '3':
                        self.user_team.all_star_statistics()
                        print("-----------------------------------------------------------------------------------------")
                        time.sleep(1)
                    elif user_option_sub_menu == '4':
                        self.user_team.game_margin_statistics()
                        print("-----------------------------------------------------------------------------------------")
                        time.sleep(1)
                except (TypeError, ValueError) as e:
                    print(' Not a valid option. Choose again')
                    continue

            elif user_option_main_menu == '3':
                a = self.user_team.monthly_win_loss()
                elements = len(self.user_team.team_row.columns)
                self.user_team.data_visual.linechart(a, elements)
                print("\n -> See graph in plots.png \n ")
                print("-----------------------------------------------------------------------------------------")
                time.sleep(1)
                continue

            elif user_option_main_menu == '4':
                while True:
                    game=input(' Where does the first team play? (enter 1 or 2) \n 1. Home \n 2. Road \n' )
                    if game == '1' or game == '2':
                        break
                    else:
                        print(' This is not a valid option! Try again!')
                        continue

                while True:
                    opp_team = input(" Enter the opposing team name or press 'T' to show all teamnames: ").title()
                    self.user_team_opp = Team(opp_team)
                    #print(self.team_row)
                    if opp_team == 'T':
                        self.print_team_names()
                    elif len(self.user_team_opp.team_row) == 0:
                        print(' This is not a valid team name!')
                        continue
                    else:
                        break

                predict= GamePredictor(self.user_team, game, opp_team)
                predict.predict()
                time.sleep(1)
                continue

            elif user_option_main_menu =='q':
                quit()

            else:
                print("\n This is not a valid option! Please try again")
                continue
