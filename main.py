from get_data import *
from team_analysis import *
from menu import *

print("-----------------------------------------------------------------------------------------")
print(" Welcome to the NBA analytics program ! \n\n Here you will have the choice between different categories, ranging from data analytics to a game result predictor.\n")
print(" First you will be asked to enter 2 info: \n")
print('\t' * 1 + '1. Your season of interest \n\n' '\t' * 1 + '2. Your team of interest \n\n Then you will be able to choose different options from the menu')
print("-----------------------------------------------------------------------------------------")
data = GetData()
data.html_code_stored_in_a_file()
data.replace()
data.create_csv()
user_menu = Menu()
user_menu.user_menu()
