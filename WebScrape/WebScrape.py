import requests
from  bs4 import BeautifulSoup


def risersAndFallers(URL):
    rarr = []
    page = requests.get(URL)
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
        #print(arr)
        rarr.append(arr)
    return rarr

if __name__ == "__main__":
    # First page of risers and fallers (t-1)
    URL = "https://www.sharesmagazine.co.uk/market-scan/risers-fallers?page=1"
    # First page of volume spikes relative to monthly average
    #URL = "https://www.sharesmagazine.co.uk/market-scan/volume-analysis?dateComparison=2&index=UKX&volumePctChange=%2C&price=%2C&pricePctChange=&sortBy=volumePctChange&sortDirection=volumeIncrease&filtersubmitbtn=Update"
    # First page of constant risers (3 consecutive days of rises)
    #URL = "https://www.sharesmagazine.co.uk/market-scan/constant-risers-fallers?page=1&sortBy=risers&days=3&filtersubmitbtn=Update"
    # First page of monthly highs
    #URL = "https://www.sharesmagazine.co.uk/market-scan/highs-lows?page=1&highLow=high&period=monthly&filtersubmitbtn=Update"
    # First page of risers and fallers (t-4w)
    #URL = "https://www.sharesmagazine.co.uk/market-scan/risers-fallers?dateComparison=2020-07-15&sortDirection=risers&index=&price=%2C&filtersubmitbtn=Update"
    listOfRisersFallers = risersAndFallers(URL)
    print(listOfRisersFallers)