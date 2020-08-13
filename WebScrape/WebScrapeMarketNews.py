import WebScrapeCommon as WSC
import requests
from  bs4 import BeautifulSoup


def marketNews(URL):
    rarr = []
    keys = ['date','news','src']
    include_cols = "2,3,4"
    rarr.append(keys)
    page = requests.get(URL)
    soup  = BeautifulSoup(page.content, "html.parser")
    mt = soup.find('table', class_='table-1')
    for t in mt.find_all("tr"):
        values = []
        elems = t.children
        i = 0
        for e in elems:
            if (e.name == 'td'):
                i=i+1
                if ( include_cols.find(str(i)) ):
                    values.append( e.text.strip(' \n\t'))
        rarr.append(values)
    return rarr

if __name__ == "__main__":
    # Market News page
    URL = "https://www.sharesmagazine.co.uk/shares/share/7DIG/news/market"
    marketNewsList = marketNews(URL)
    print(marketNewsList)