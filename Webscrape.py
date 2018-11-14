from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.premierleague.com/matchweek/3270/table"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

filename = "premier_league_table.csv"
f = open(filename, "w")

headers = "position, team, points\n"
f.write(headers)

page_soup = soup(page_html, features="html.parser")
tableRows = page_soup.findAll("tr",{"data-filtered-table-row": "26"})
for row in tableRows:
    position = row.find(class_="pos").get_text()
    team = row.find(class_="team").get_text()
    points = row.find(class_="points").get_text()
    print (position + " " + team + " " + points)
    #write to csv file
    f.write(position + "," + team + "," + points + "\n")

f.close()



