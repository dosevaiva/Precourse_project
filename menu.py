from team_analysis import *

class Menu():

    def __init__(self):
        self.user_team = Team()

    def user_menu(self):
        while True:
            print('What metric do you want to see? \n 1. Win/loss ratio \n 2. Conference statistics \n 3. Division statistics \n 4. All-Star statistics \n 5. Game margin statistics \n 6. Monthly graph \n 7. Game result predictor \n\n OR type Q to quit \n')
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
                self.user_team.conference_statistics()
                continue
            elif user_option_main_menu == '3':
                self.user_team.division_statistics()
                continue
            elif user_option_main_menu == '4':
                self.user_team.all_star_statistics()
                continue
            elif user_option_main_menu == '5':
                self.user_team.game_margin_statistics()
                continue
            elif user_option_main_menu == '6':
                a = self.user_team.monthly_win_loss()
                self.user_team.data_visual.linechart(a)
                continue
            elif user_option_main_menu == '7':
                continue
            elif user_option_main_menu =='q':
                quit()
            else:
                print("\nThis is not a valid option! Please try again!")
                continue
