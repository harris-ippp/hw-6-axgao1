#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
import requests

resp = requests.get('http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General')
html = resp.content
soup = bs(html, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr', 'election_item') #finds all table rows with class 'election_item'

yearlist=[]
for row in rows:
    yearlist.append(row.contents[1].text) #creates list of years

idlist=[]
for i in range(len(rows)):
    idlist.append(rows[i]['id'][-5:]) #creates list of ids by just getting last 5 digits, the id
