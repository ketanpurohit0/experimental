import WebScrapeCommon as WSC
import requests
from  bs4 import BeautifulSoup


def fundamentals(URL):

    page = requests.get(URL)


    soup  = BeautifulSoup(page.content, "html.parser")
    mt = soup.find('table', class_='table-1 th-grey gutter-under-large fundamentalsTable vert-table')
    map = {}
    keys = []
    values = []
    for t in mt.find_all("tr"):
        #print("*",t)
        elems = t.children
        for e in elems:
            #print("*", e.name, e.string)
            if (e.name == 'th'):
                keys.append(e.string.strip(' \n\t'))
            elif (e.name == 'td'):
                values.append(e.string.strip(' \n\t'))
    #print(keys, values)
    zipped_kv =zip(keys, values)
    for item in zipped_kv:
        map[item[0]] = WSC.optionalNumeric(item[1])
    return map

if __name__ == "__main__":
    # Fundamentals page
    URL = "https://www.sharesmagazine.co.uk/shares/share/7DIG/fundamentals"
    fundamentalsMap = fundamentals(URL)
    print(fundamentalsMap)
    #zz=str(fundamentalsMap)
    #pass