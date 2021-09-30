from get_data import *
from team import *
from menu import *

print("-----------------------------------------------------------------------------------------")
print(" Welcome to the NBA analytics program ! \n\n Here you will have the choice between different categories, ranging from data analytics to a game result predictor.\n")
print(" First you will be asked to enter 2 info: \n")
print('\t' * 1 + '1. Your season of interest \n\n' '\t' * 1 + '2. Your team of interest \n\n Then you will be able to choose different options from the menu')
print("-----------------------------------------------------------------------------------------")

while True:
    season = input(" Please enter the year of the season: ")
    if season.isdigit():
        if int(season) > 2020 or int(season) < 2005:
            print('Please input a year between 2005 and 2020!')
            continue
        else:
            url = 'https://www.basketball-reference.com/leagues/NBA_{}_standings.html'.format(season)
        break
    else:
        print('Please input a year between 2005 and 2020!')
        continue

data = GetData(season,url)
user_menu = Menu()

