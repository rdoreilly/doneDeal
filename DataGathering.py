import requests
import re
from bs4 import BeautifulSoup

# URL we are looking for
url = "https://www.donedeal.ie/cars/Ford/C-MAX?start=1"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)

queryURLS = []
# PULL THE 1st card-collection from the page as there is a 2nd with advertisments.
# More info on regex to be found below
# https://stackoverflow.com/questions/499345/regular-expression-to-extract-url-from-an-html-link
soup = BeautifulSoup(response.content, 'html.parser')
for tag in soup.findAll('a', href=True, class_="card__link"):
    queryURLS.append(tag['href'])
#print(queryURLS)



count=0
#Pull data from each of the pages
for url in queryURLS:
    print(url)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    #file = open("data/car"+str(count)+".html","w")
    count += 1

    #title = soup.findAll("h1", {"itemprop":"name"})
    #print(title)

    #content = soup.prettify()
    #print(content)
    #file.write(content)
    #file.close()



    #print(soup.prettify())

    title = soup.findAll("title")
    print(title)
    #price = soup.findAll("span", {"class" : "price ng-binding"})
    #print(price)
    #county = soup.findAll('span', class_="county-disp ng-binding")

    #print(price)
    #print(county)


    #main-content page-row ng-scope
    #< h1 itemprop = "name" ng-bind-html = "adView.ad.header" class ="ng-binding" > Ford C-Max < / h1 >
    #<span class="county-disp ng-binding">Offaly</span>
    #<span class ="price ng-binding" > 999 < / span >

#    class ="cad-content divider"

#class="cad-info-container space-top-10"