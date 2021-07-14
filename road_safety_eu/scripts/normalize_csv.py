from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_data():
    data_url = 'https://en.wikipedia.org/wiki/Road_safety_in_Europe'
    data_id = 'wikitable sortable'

    response = requests.get(data_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    roadSafetyTable = soup.find('table', {'class' : data_id})
    rows = roadSafetyTable.find_all('tr')
    columns = [v.text.replace('\n', '') for v in rows[0].find_all('th')]

    df = pd.DataFrame(columns=columns)
    
    for i in range(1,len(rows)):
        tds = rows[i].find_all('td')

        if len(tds)==4:
            values = [tds[0].text, tds[1].text, tds[2].text, tds[3].text.replace('\n',''.replace('\xa0',''))]
        else:
            values = [td.text.replace('\n',''.replace('\xa0','')) for td in tds]

        df = df.append(pd.Series(values, index=columns), ignore_index=True)
    
    df = df.rename(columns={
        'Area(thousands of km2)[24]':'Area',
        'Population in 2018[25]':'Population',
        'GDP per capita in 2018[26]':'GDP per capita',
        'Population density(inhabitants per km2) in 2017[27]':'Population density',
        'Vehicle ownership(per thousand inhabitants) in 2016[28]':'Vehicle ownership',
        'Total Road Deaths in 2018[30]':'Total road deaths',
        'Road deathsper Million Inhabitants in 2018[30]':'Road deaths per Million Inhabitants'}) 

    df = df.filter(['Country','Area','Population', 'GDP per capita', 'Population density','Vehicle ownership','Total road deaths', 'Road deaths per Million Inhabitants']) 
    df['Year'] = pd.Series([2018 for x in range(len(df.index))])

    df.to_csv("road_safety_eu/data/data.csv", sep=',')
    return df

print(get_data())  
