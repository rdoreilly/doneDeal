
# new url
url = 'https://www.donedeal.ie/cars-for-sale/ford-c-max-low-millage-tax-and-nct/21023989?campaign=3'

with ul.urlopen(url) as f:
    print(f.read().decode('utf-8'))


# read all data
#print(ul.urlopen(url).read())


#session = HTMLSession()
#r = session.get(url)

#r = session.get('https://www.donedeal.ie/cars-for-sale/ford-c-max-low-millage-tax-and-nct/21023989?campaign=3')
#print(r.html.links)
#about = r.html.find('#about', first=True)
"""
page = r.html.render()
print(page)
metaData = page.find('.meta-info__value')
#metaData = r.html.find('#about', first=True)
print(metaData)
"""
#print(r.html.render().text)

#r.html.search('Make ')[0]
#<div class="cad-details cad-details-spacing">
#/ html / body / main / div / div[1] / div / div[2] / div[2] / div[4] / div[1] / div[2] / ul



#sel = 'body > main > div > div:nth-child(1) > div > div.main-content.page-row.ng-scope > div.cad-column-1 > div:nth-child(4) > div.cad-details.cad-details-spacing > div.cad-content.divider > ul > li:nth-child(2) > span.meta-info__value > span'

#print(type(r.html.find(sel, first=True)))
#GitHub is a development platform inspired by the way you work. From open source to business, you can host and review code, manage projects, and build software alongside millions of other developers.

#Make Ford
#Model C-MAX
#Year 2004



#file = open("carJson1.html","a")
#from urllib.request import urlopen
#with urlopen(url) as response:
#    for line in response:
#        line = line.decode('utf-8')  # Decoding the binary data to text.
#        file.write(line)
#file.close()

#print(page)



# convert json text to python dictionary
#data = json.loads(page)

#print(data)