import requests 
from bs4 import BeautifulSoup

url ="https://www.mygov.in/corona-data/covid19-statewise-status"
req = requests.get(url)

bs = BeautifulSoup(req.text,"html.parser")

data= bs.find_all("div",class_="field-item odd")

maharashtra = data[7].text
Confirmed  =42 # index = 42
Discharged = 73 # index = 73
Deaths = 83 # index = 83

confirmed = int(maharashtra[int(Confirmed):46])
discharged = int(maharashtra[int(Discharged):76])
deaths = int(maharashtra[int(Deaths):])

print("===MAHARASHTRA REPORT COVID-19===")
print("Total number of confermed cases:",confirmed)
print("Total dischargged:",discharged)
print("Total deaths:",deaths)