from game_predictor import GamePredictor
from team_analysis import *

class Menu():

    def __init__(self):
        #put this is menu
        while True:
            self.team_name = input("Please enter the official name of an NBA team: ").title()
            self.user_team = Team(self.team_name)
            #print(self.team_row)

            if len(self.user_team.team_row) == 0:
                print('This is not a valid team name!')
                continue
            else:
                break

    def user_menu(self):
        while True:
            print('\n What metric do you want to see? \n\n 1. Win/loss ratio \n 2. Overall statistics \n 3. Monthly graph \n\n OR enter 4 if you want to access the Game Result Predictor \n\n OR type Q to quit \n')
            user_option_main_menu = input("What option are you choosing? ").lower()

            if user_option_main_menu == '1':
                print('What metric do you want to see? \n 1. Overall win ratio \n 2. Home win ratio \n 3. Road win ratio \n\n OR press any button to go back to the main menu!\n')
                user_option_sub_menu=input('Input a number between 1 and 3: ')
                try:
                    user_option_sub_menu = int(user_option_sub_menu)
                    if user_option_sub_menu < 1 or user_option_sub_menu > 3:
                        print('This is not a valid option!')
                    else:
                        a = self.user_team.win_loss_ratio(user_option_sub_menu)
                        self.user_team.data_visual.piechart_win_loss_ratio(a[0], a[1], a[3])
                except (TypeError, ValueError) as e:
                    print('Not a valid option. Choose again')
                    continue

            elif user_option_main_menu == '2':
                print("What category of statistics do you want to see? \n 1. Conference \n 2. Division \n 3. All-Star \n 4. Game margin")
                print('')
                user_option_sub_menu = input('Input a number between 1 and 4: ')
                print('')
                try:
                    if user_option_sub_menu == '1':
                        self.user_team.conference_statistics()
                    elif user_option_sub_menu == '2':
                        self.user_team.division_statistics()
                    elif user_option_sub_menu == '3':
                        self.user_team.all_star_statistics()
                    elif user_option_sub_menu == '4':
                        self.user_team.game_margin_statistics()
                except (TypeError, ValueError) as e:
                    print('Not a valid option. Choose again')
                    continue

            elif user_option_main_menu == '3':
                a = self.user_team.monthly_win_loss()
                elements = len(self.user_team.team_row.columns)
                self.user_team.data_visual.linechart(a, elements)
                continue

            elif user_option_main_menu == '4':

                game = input('Where does the first team play? \n 1. Home \n 2. Road \n' )
                opp_team = input("Enter the opposing team: ").title()
                predict = GamePredictor(self.user_team, game, opp_team)
                predict.predict()
                continue

            elif user_option_main_menu =='q':
                quit()

            else:
                print("\nThis is not a valid option! Please try again!")
                continue
