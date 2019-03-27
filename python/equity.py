import requests
import pandas as pd
from bs4 import BeautifulSoup
#Base_url=("https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp")
Base_url=("https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=TATASTEEL")
page=requests.get(Base_url)
#page.status_code
#page.content
soup=BeautifulSoup(page.content,'html.parser')
#print(soup.prettify())
#elem = soup.findAll('totalBuyQuantity', {'title': 'title here'})
#elem = soup.find_all("total")
#print(elem)
price=soup.find('div',attrs={'id':'responseDiv'})
print(price)
#value=soup.find(attrs={'totalBuyQuantity' : 'MYCLASS'})
#hit = value.text.strip()
#print(hit)
#price=price.attrs['tradedDate']
#print(price)
