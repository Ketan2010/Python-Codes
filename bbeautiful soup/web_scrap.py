#try scraping from hosted website on google
from bs4 import BeautifulSoup
import requests



url="https://internshala.com/internships"
source=requests.get(url).text
soup=BeautifulSoup(source,'lxml')
#print(soup.prettify)

internships=soup.find_all('div',class_='company')

for internship in internships:
    print("=========================================")
    print("internship name:",internship.h4.a.text)

##### output #####
#=========================================
#internship name: Social Media Marketing
#=========================================
#internship name: Mobile App Development
#=========================================
#internship name: Business Development (Sales)
#=========================================
#internship name: Social Media Marketing
#=========================================
#internship name: Anchoring
#and many more--------









