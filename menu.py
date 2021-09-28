from team_analysis import *

class Menu():

    def __init__(self):
        self.user_team = Team()

    def user_menu(self):
        while True:
            print('What metrix do you want to see? \n 1. Win/loss ratio \n 2. Division comparison \n 3. Monthly graph \n 4. Coference statistics \n 5. Game result predictor \n\n OR type Q to quit \n')
            user_option_main_menu = input("What option are you choosing? ").lower()

            if user_option_main_menu == '1':
                print('What metrix do you want to see? \n 1. Overall win ratio \n 2. Home win ratio \n 3. Road win ratio \n\n OR press any button to go back to the main menu!\n')
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
                continue
            elif user_option_main_menu == '3':
                a = self.user_team.monthly_win_loss()
                self.user_team.data_visual.linechart(a)
                continue
            elif user_option_main_menu == '4':
                continue
            elif user_option_main_menu == '5':
                continue
            elif user_option_main_menu =='q':
                quit()
            else:
                print("\nThis is not a valid option! Please try again!")
                continue
