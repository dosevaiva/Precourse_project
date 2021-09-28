from get_data import *
from team_analysis import *
from menu import *

data = GetData()
data.html_code_stored_in_a_file()
data.replace()
data.create_csv()
user_menu = Menu()
user_menu.user_menu()

