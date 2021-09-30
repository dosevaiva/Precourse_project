

import matplotlib.pyplot as plt
import numpy as np

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
        plt.show()
        plt.close()

    def linechart(self,y,elements):
        num_elements = elements - 16
        x = np.linspace(1,100,num_elements)
        x_text = ['Oct', 'Nov','Dec','Jan','Feb','Mar','Jul','Aug']
        x_text_new =[]
        for i in range(num_elements):
            x_text_new.append(x_text[i])

        plt.figure()
        plt.title('Monthly performance graph')
        plt.ylabel('%')
        plt.xticks(x,x_text_new)
        plt.plot(x,y)
        plt.savefig('plots.png')
        plt.show()
        plt.close()
