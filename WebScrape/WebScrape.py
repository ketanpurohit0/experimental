import requests
from  bs4 import BeautifulSoup

URL = "https://www.sharesmagazine.co.uk/market-scan/risers-fallers?page=2"
page = requests.get(URL)

#<div class="market-table">
#<tbody>
#<tr>
#print(page.text)
soup  = BeautifulSoup(page.content, "html.parser")
mt = soup.find('div', class_='market-table')
tbody= mt.find("tbody")
for t in tbody.find_all("tr"):
    #print("*",t)
    arr = []
    elems = t.find_all("td")
    for e in elems:
        a  = e.find('a')
        if (a is not None):
            #print("@",a.attrs['href'])
            arr.append(a.attrs['href'])
        #print("@", e.text)
        arr.append(e.text)
    print(arr)

