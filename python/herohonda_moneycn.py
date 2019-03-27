import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import bs4

from fastnumbers import isfloat
from fastnumbers import fast_float
from multiprocessing.dummy import Pool as ThreadPool

import matplotlib.pyplot as plt
import seaborn as sns
import json

def ffloat(string):
    if string is None:
        return np.nan
    if type(string)==float or type(string)==np.float64:
        return string
    if type(string)==int or type(string)==np.int64:
        return string
    return fast_float(string.split(" ").replace(',','').replace('%',''),
                      default=np.nan)
def get_scrip_info(url):
    original_url=url
    key_val_pairs={}
    
    page_response=requests.get(url,timeout=240)
    page_content=BeautifulSoup(page_response.content,"html.parser")
    price=ffloat(page_content.find('div',attrs={'id':'Nse_Prc_tick_div'}).text)
    key_val_pairs['price']=price
    return key_val_pairs

a=get_scrip_info("https://www.moneycontrol.com/india/stockpricequote/auto-2-3-wheelers/heromotocorp/HHM")
print(a)
