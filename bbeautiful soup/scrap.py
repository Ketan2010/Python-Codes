from bs4 import BeautifulSoup
import requests
#refer html code of sample.html
with open('sample.html') as html_file:
    soup=BeautifulSoup(html_file,'lxml')

#this will give only first div in html
tit=soup.div
print("===================================================================")
print(tit)
#to get only text in div without html element tag
tit=soup.div.text
print("===================================================================")
print(tit)

print("===================================================================")
match=soup.find('div',class_='footer').text
print(match)

#to find div with class name
#this will print only first div with that class name
print("===================================================================")
document=soup.find('div',class_='card2').h2.text
print(document)


#to get href/src from tag
print("===================================================================")
document1=soup.find('div',class_='card2').a ['href']
print(document1)

#to prinr all div with same class name
#use find_all() method
print("===================================================================")
doclist=soup.find_all('div',class_='card2')
for doc in doclist:
    print("book name:",doc.h2.text)
    print("Auther name:",doc.h5.text)



#### OUTPUT ####
#===================================================================
#<div class="card1">
# <h1 style=" background-image: linear-gradient(to right, #00cc00 ,  #009900,#006600,#003300);">TOP 10 BOOKS</h1>
# </div>
# ===================================================================

# TOP 10 BOOKS

# ===================================================================

#         "Make Books your Best FRIEND,
# It Will Never Hurt You"



# ===================================================================
# 1.Leaving Time
# ===================================================================
# https://www.jodipicoult.com/leaving-time.html
# ===================================================================
# book name: 1.Leaving Time
# Auther name: Auther:Jodi Picoult,A Novel
# book name: 2.1st to Die
# Auther name: Auther:James Patterson,A Novel