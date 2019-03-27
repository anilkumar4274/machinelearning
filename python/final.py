#import requests
#import pandas as pd
#from bs4 import BeautifulSoup
#Base_url=("https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=TATASTEEL")
#page=requests.get(Base_url)
#soup=BeautifulSoup(page.content,'html.parser')
#price=soup.find('div',attrs={'id':'responseDiv'})
#print(price)
#url=("https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=TATASTEEL")
#dfs1 = pd.read_html(url, attrs={'id': 'table'})
#dfs2 = pd.read_html(url, attrs={'class': 'sortable'})
#print(np.array_equal(dfs1[0], dfs2[0]))  
#print(dfs1)
import requests
import pandas as pd
url='https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=TATASTEEL'
#url = 'https://www.investing.com/earnings-calendar/'
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}
r = requests.get(url, headers=header)
#dfs = pd.read_html(r.text,attrs={'id':'responseDiv'})
dfs = pd.read_html(r.text)
#print(dfs[5].transpose())
print(dfs[5])
