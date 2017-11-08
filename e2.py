#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
import requests

resp = requests.get('http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General')
html = resp.content
soup = bs(html, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr', 'election_item')

yearlist=[]
for row in rows:
    yearlist.append(row.contents[1].text)

idlist=[]
for i in range(len(rows)):
    idlist.append(rows[i]['id'][-5:])

#referenced code from e1 for arguments idlist and yearlist

base = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'

dictionary = dict(zip(idlist, yearlist)) #zip returns tuples using iterators, converted to a dictionary

for id in idlist: #looping over iterables from e1, similar to 'for line in open("ELECTION_ID")'
    lastyear_url = base.format(id)
    resp = requests.get(lastyear_url).text
    file = dictionary[id] + ".csv" #creates file with year name and format with content from responses from all urls

    with open(file,'w') as output:
        output.write(resp)
