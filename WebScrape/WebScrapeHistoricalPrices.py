import WebScrapeCommon as WSC
import requests
from  bs4 import BeautifulSoup


def historicalPrices(URL):
    rarr = []
    keys = ['date','close']
    include_cols = [1,5]
    methodMap = dict({1: WSC.standardizeDate, 5: WSC.optionalNumeric})
    rarr.append(keys)
    page = requests.get(URL)
    soup  = BeautifulSoup(page.content, "html.parser")
    mt = soup.find('table', class_='footable-table table-1 gutter-under gutter-top-small')
    tbody = mt.find("tbody")
    for t in tbody.find_all("tr"):
        rarr.append([methodMap[i](t.select(f"td:nth-of-type({str(i)})")[0].text) for i in include_cols])       
    return rarr

if __name__ == "__main__":
    # Historical Prices
    URL = "https://www.sharesmagazine.co.uk/shares/share/7DIG/historic-prices"
    historicalPricesList = historicalPrices(URL)
    print(historicalPricesList)