import requests
from  bs4 import BeautifulSoup

def optionalNumeric(s):
    try:
        return float(s)
    except ValueError:
        return s

# Fundamentals page
URL = "https://www.sharesmagazine.co.uk/shares/share/7DIG/fundamentals"

page = requests.get(URL)

#<div class="market-table">
#<tbody>
#<tr>
#print(page.text)
soup  = BeautifulSoup(page.content, "html.parser")
mt = soup.find('table', class_='table-1 th-grey gutter-under-large fundamentalsTable vert-table')
map = {}
for t in mt.find_all("tr"):
    #print("*",t)
    keys = []
    values = []
    elems = t.children
    for e in elems:
        print("*", e.name, e.string)
        if (e.name == 'th'):
            keys.append(e.string.strip(' \n\t'))
        elif (e.name == 'td'):
            values.append(e.string.strip(' \n\t'))
    print(keys, values)
    x=zip(keys, values)
    for item in x:
        map[item[0]] = optionalNumeric(item[1])
print(map)

