import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
Base_url=("https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=TATASTEEL")
page=requests.get(Base_url)
soup=BeautifulSoup(page.content,'html.parser')
price=soup.find('div',attrs={'id':'responseDiv'})
print(price)
