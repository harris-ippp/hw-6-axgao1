#!/usr/bin/env python

import pandas as pd

#chmod +x ex3.py

header = pd.read_csv("1924.csv", nrows = 1).dropna(axis = 1)

d = header.iloc[0].to_dict()

df = pd.read_csv("1924.csv", index_col = 0, thousands = ",", skiprows = [1])

df.rename(inplace = True, columns = d) # rename to democrat/republican

df.dropna(inplace = True, axis = 1)    # drop empty columns

df = df[["Democratic", "Republican", "Total Votes Cast"]] #reassigns dataframe as dataframe with just these 3 columns

df["Year"] = 1924 #adds Year column with just 1924s

allyears = ['1928', '1932', '1936', '1940', '1944','1948', '1952', '1956', '1960', '1964', '1968','1972', '1976', '1980', '1984', '1988','1992','1996','2000', '2004', '2008', '2012', '2016']
#create list for iteration starting in 1928 because 1924 was already used for initial dataframe

for yeardf in allyears:
    filename = yeardf + ".csv"
    header = pd.read_csv(filename, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    tempdf = pd.read_csv(filename, index_col = 0, thousands = ",", skiprows = [1])
    tempdf.rename(inplace = True, columns = d) # rename to democrat/republican
    tempdf.dropna(inplace = True, axis = 1)    # drop empty columns
    tempdf = tempdf[["Democratic", "Republican", "Total Votes Cast"]]
    tempdf["Year"] = int(yeardf) #creates more Year columns for all years with iterable after years are converted to integers
    df = df.append(tempdf)

#print(df)

df['RepublicanShare'] = df['Republican']/df['Total Votes Cast'] #dividing Republican by Total Votes Cast gives RepublicanShare

Accomackdf = df.loc['Accomack County'] #uses county name as index to create new dataframe with specific county data
accomackgraph = Accomackdf.plot(x = "Year", y = "RepublicanShare", legend = False, title = "Accomack Republican Vote Share")
accomackgraph.set_ylabel("Republican Vote Share")
accomackgraph.figure.savefig('accomack_county.pdf')

Albemarledf = df.loc['Albemarle County']
albemarlegraph = Albemarledf.plot(x = "Year", y = "RepublicanShare", legend = False, title = "Albemarle Republican Vote Share")
albemarlegraph.set_ylabel("Republican Vote Share")
albemarlegraph.figure.savefig('albemarle_county.pdf')

AlexandriaCitydf = df.loc['Alexandria City']
alexandriacitygraph = AlexandriaCitydf.plot(x = "Year", y = "RepublicanShare", legend = False, title = "Alexandria City Republican Vote Share")
alexandriacitygraph.set_ylabel("Republican Vote Share")
alexandriacitygraph.figure.savefig('alexandriacity_county.pdf')

Alleghanydf = df.loc['Alleghany County']
alleghanygraph = Alleghanydf.plot(x = "Year", y = "RepublicanShare", legend = False, title = "Alleghany Republican Vote Share")
alleghanygraph.set_ylabel("Republican Vote Share")
alleghanygraph.figure.savefig('alleghany_county.pdf')
