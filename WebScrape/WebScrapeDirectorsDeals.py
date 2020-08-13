import WebScrapeCommon
import requests
from  bs4 import BeautifulSoup


def directorsDeals(URL):
    rarr = []
    keys = ['date','type', 'dir','pos', 'volp','value']
    rarr.append(keys)
    page = requests.get(URL)
    soup  = BeautifulSoup(page.content, "html.parser")
    mt = soup.find('table', class_='table-1 director-deals-sm')
    tbody= mt.find("tbody")
    for t in tbody.find_all("tr"):
        values = []
        elems = t.children
        for e in elems:
            if (e.name == 'td'):
                values.append(e.text.strip(' \n\t'))
        rarr.append(values)
    return rarr

if __name__ == "__main__":
    # Fundamentals page
    URL = "https://www.sharesmagazine.co.uk/shares/share/7DIG/director-deals"
    directorsDealsList = directorsDeals(URL)
    print(directorsDealsList)