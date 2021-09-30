from bs4 import BeautifulSoup
import requests
import csv
import numpy as np

class GetData():

    def __init__(self,season,url):
        self.season = season
        self.url = url

    def html_code_parsing(self):

        source=requests.get(self.url).text
        soup=BeautifulSoup(source, 'lxml')

        file=open('html_code.html','w', encoding='UTF-8')
        file.write(soup.prettify())
        file.close

    def replace(self):
        with open('html_code.html', 'r', encoding='UTF-8') as html_file:
            file_content = html_file.read()
            file_content= file_content.replace(" <!--", "")
        with open('html_code.html', 'w', encoding='UTF-8') as html_file:
            html_file.write(file_content)

    def find_table(self,html_file):
        soup = BeautifulSoup(html_file, 'lxml')
        #print(soup)
        table = soup.find(class_='sortable stats_table')
        return table

    def get_headers(self,table):
        headers = []
        #find all headings
        for i in table.thead.find('tr', class_=False):
            title=i.string.strip()
            headers.append(title)

            # remove the Rk heading
            headers2=headers[2:]
            #remove empty elements from the list of headings
            new_headers = list(filter(None, headers2))

        return new_headers

    def find_rows(self,table):
        rows = []
        #get all the data from the table rows
        for tr in table.tbody.findAll('tr'):
            for td in tr.findAll('td'):
                value = td.text
                rows.append(value)
        #split the data into 30 lists because we have 30 teams
        spli_team = np.array_split(rows,30)

        for array in spli_team:
            b = (list(array))
            #print(b)
        return spli_team

    def create_csv(self):
        #open the file
        with open('html_code.html', encoding='UTF-8') as html_file:
            table = self.find_table(html_file)
            headers = self.get_headers(table)
            csv_file = open('nba_test.csv', 'w', encoding='UTF-8')
            #create a writer
            csv_writer = csv.writer(csv_file)
            #write the headings to the csv file
            csv_writer.writerow(headers)
            r = self.find_rows(table)

            for array in r:
                b = (list(array))
                #add the rows to the csv file
                csv_writer.writerow(b)

        #close the file
        csv_file.close()
