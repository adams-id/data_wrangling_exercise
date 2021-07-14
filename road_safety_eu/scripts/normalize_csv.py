from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_data():
    #Store the data url and table in a variable to be used later
    data_url = 'https://en.wikipedia.org/wiki/Road_safety_in_Europe'
    data_id = 'wikitable sortable'

    #Send a request to get the data from the data_url link 
    response = requests.get(data_url)

    #Using the BeautifulSoup library to store and parse out the data recieved from the get request 
    soup = BeautifulSoup(response.text, 'html.parser')

    #using the find method to specifically select the table with the specified class attribute and storing into a variable  
    road_safety_table = soup.find('table', {'class' : data_id})
    #Autopopulate the row span technique to set a new row after the data from each previous tag has been set 
    rows = road_safety_table.find_all('tr')

    #Setting the column header as the first row of the raw data returned and replacing the \n string from the header names with an empty string
    columns = [v.text.replace('\n', '') for v in rows[0].find_all('th')]
    df = pd.DataFrame(columns=columns)

    # Extract every row with corresponding columns then append the values to the create pd dataframe "df". 
    # The first row with index 0 is skipped because it is already the header
        
    for i in range(1,len(rows)):
        tds = rows[i].find_all('td')

        if len(tds)==4:
            values = [tds[0].text, tds[1].text, tds[2].text, tds[3].text.replace('\n',''.replace('\xa0',''))]
        else:
            values = [td.text.replace('\n',''.replace('\xa0','')) for td in tds]

        df = df.append(pd.Series(values, index=columns), ignore_index=True)

    #Rename the columns to the essential headings using the rename method
    df = df.rename(columns={
        'Area(thousands of km2)[24]':'Area',
        'Population in 2018[25]':'Population',
        'GDP per capita in 2018[26]':'GDP per capita',
        'Population density(inhabitants per km2) in 2017[27]':'Population density',
        'Vehicle ownership(per thousand inhabitants) in 2016[28]':'Vehicle ownership',
        'Total Road Deaths in 2018[30]':'Total road deaths',
        'Road deathsper Million Inhabitants in 2018[30]':'Road deaths per Million Inhabitants'}) 

    #Filter the DataFrame to return only the requested columns from the challenge
    df = df.filter(['Country','Area','Population', 'GDP per capita', 'Population density','Vehicle ownership','Total road deaths', 'Road deaths per Million Inhabitants']) 
    
    #Adding a Year column of constant value 2018 
    df['Year'] = pd.Series([2018 for x in range(len(df.index))])
    
    #Sort the dataset from index 0 to 27 leaving out the EU Total row as this would always be the bottom row
    sorted_table = df[0:27].sort_values('Road deaths per Million Inhabitants')
    #Adding the EU row data to the sorted table and storing in the dataset 
    df = sorted_table.append(df.loc[28])  
    
    #Remove the index value from the data set and setting the Country values as the first column 
    df = df.set_index('Country')

    #Storing the dataset to a csv file with the path name included and the delimiter as ','
    df.to_csv("road_safety_eu/data/data.csv", sep=',')
    return df

print(get_data())  
