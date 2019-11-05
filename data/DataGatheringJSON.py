import urllib.request as ul
from bs4 import BeautifulSoup
import json
from requests_html import HTMLSession

#Car from DoneDeal
url = 'https://www.donedeal.ie/cars-for-sale/ford-c-max-low-millage-tax-and-nct/21023989?campaign=3'
url2 = 'https://www.donedeal.ie/cars-for-sale/ford-c-max-1-6tdci-95ps-active-32-per-week/20830960'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
session = HTMLSession()
r = session.get(url, headers=headers)

#TESTED FOLLOWING LINE WORKS
#print(r.html.links)

r.html.render()

#TESTED FOLLOWING LINE WORKS
sel = 'head'
print(r.html.find(sel, first=True).text)

#TESTED FOLLOWING LINE WORKS if PAGE RENDERED
sel = 'head > title'
print(r.html.find(sel, first=True).text)

count = 1
while count < 15:
          # This value varies - why??? As the page is rendering, I should be able to improve my scrapping to pull the last tag.
            #body > main > div > div: nth - child(1) > div > div.main - content.page - row.ng - scope > div.cad - column - 1 > div:nth - child(5) > div.cad - details.cad - details - spacing > div.cad - content.divider > ul > li: nth - child(1) > span.meta - info__value > span
    sel = '* > li:nth-child(' + str(count) + ') > span.meta-info__value > span'
    print(r.html.find(sel, first=True).text)
    count+=1
#sel = 'body > main > div > div:nth-child(1) > div > div.main-content.page-row.ng-scope > div.cad-column-1 > div:nth-child(4) > div.cad-details.cad-details-spacing > div.cad-content.divider > ul > li:nth-child(1) > span.meta-info__value > span'
#sel = 'body > main > div > div:nth-child(1) > div > div.main-content.page-row.ng-scope > div.cad-column-1 > div:nth-child(4) > div.cad-details.cad-details-spacing > div.cad-content.divider > ul > li:nth-child(2) > span.meta-info__value > span'
#sel2 = 'body > main > div > div:nth-child(1) > div > div.main-content.page-row.ng-scope > div.cad-column-1 > div:nth-child(4) > div.cad-details.cad-details-spacing > div.cad-content.divider > ul > li:nth-child(3) > span.meta-info__value > span'
# body > main > div > div:nth-child(1) > div > div.main-content.page-row.ng-scope > div.cad-column-1 > div:nth-child(4) > div.cad-details.cad-details-spacing > div.cad-content.divider > ul > li:nth-child(14) > span.meta-info__value > span


