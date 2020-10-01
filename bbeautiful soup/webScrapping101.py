import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

headers = {'Accept-language' : 'en-US , en ; q = 0.5'}
url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"

results = requests.get(url , headers = headers)
soup = BeautifulSoup(results.text , "html.parser")
#print(soup.prettify())  #TO TEST THE SCRAPPED DATA FROM THE WEBSITE, OK TESTED.

#now we'll declare empty lists to store info from the website into some familiar data type.
titles = []
years = []
time = []
imdb_rating = []
metascore = []
votes = []
us_gross = []

#now we're trying to tell our scraper the main tag for gathering the info.
#i.e. in this case, its the "lister-item mode-advanced" div

movie_div = soup.find_all('div', class_="lister-item mode-advanced")

#now we'll try to scrap the data off the website and store it in our lists, using for loop( obv?)

for container in movie_div:
    name = container.h3.a.text     # this loop appends the names of all the movies from the website.
    titles.append(name)
    #print(titles[0])   #kul, gives the expected output :D

    year = container.h3.find('span' , class_ = 'lister-item-year').text  #extracts the year of release of movie.
    years.append(year)  # makes up our list of yearOfRelease of the movies.

    runTime = container.find('span' , class_= 'runtime').text if container.p.find('span' , class_ = 'runtime') else '-'
    time.append(runTime)    # makes up our list of runtimes of movies.

    rating = float(container.strong.text)
    imdb_rating.append(rating)   # makes up our list of imdbRatings of the movies.

    score = container.find('span', class_="metascore").text if container.find('span', class_="metascore").text else '-'
    metascore.append(score)  # caters to the metascore of the movie.

    #now the following part is a lil tricky (not for me tho lol, im just copying and trying to understand.)
    nv = container.find_all('span' , attrs = {'name' : 'nv'})

    # for votes:
    vote = nv[0].text
    votes.append(vote)

    # for gross earnings:
    gross = nv[1].text if len(nv)>1 else '-'
    us_gross.append(gross)

#print(us_gross[:6])  #OK REPORTING.
# SO NOW OUR DATA HAS BEEN FETCHED FROM THE WEBSITE AND IS IN THE RESPECTIVE LISTS.
# NOW IS THE TIME TO MAKE A PANDAS DATAFRAME FOR STORING THIS DATABASE.

moviesDataFrame = pd.DataFrame({
    'name' : titles,
    'year' : years,
    'runTime' : time,
    'imdbRating' : imdb_rating,
    'metascore' : metascore,
    'votes' : votes,
    'grossIncome' : us_gross
})

'''
print(moviesDataFrame) # WONDERFULL :")
'''
moviesDataFrame.to_csv("moviesIMDB.csv")