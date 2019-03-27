import pandas as pd
import numpy as np
a={"tradedDate":"27MAR2019","data":[{"pricebandupper":"571.25","symbol":"TATASTEEL","applicableMargin":"12.50","bcEndDate":"20-JUL-18","totalSellQuantity":"5,611","adhocMargin":"-","companyName":"Tata Steel Limited","marketType":"N","exDate":"05-JUL-18","bcStartDate":"07-JUL-18","css_status_desc":"Listed","dayHigh":"523.00","basePrice":"519.35","securityVar":"6.04","pricebandlower":"467.45","sellQuantity5":"-","sellQuantity4":"-","sellQuantity3":"-","cm_adj_high_dt":"21-SEP-18","sellQuantity2":"-","dayLow":"513.05","sellQuantity1":"5,611","quantityTraded":"43,12,714","pChange":"-1.03","totalTradedValue":"27,102.16","deliveryToTradedQuantity":"45.20","totalBuyQuantity":"-","averagePrice":"517.30","indexVar":"-","cm_ffm":"38,934.09","purpose":"ANNUAL GENERAL MEETING \/ DIVIDEND- RS 10 PER SHARE","buyPrice2":"-","secDate":"27-Mar-2019 15:00:00","buyPrice1":"-","high52":"647.60","previousClose":"519.35","ndEndDate":"-","low52":"441.35","buyPrice4":"-","buyPrice3":"-","recordDate":"-","deliveryQuantity":"19,49,162","buyPrice5":"-","priceBand":"No Band","extremeLossMargin":"5.00","cm_adj_low_dt":"29-JAN-19","varMargin":"7.50","sellPrice1":"515.80","sellPrice2":"-","totalTradedVolume":"52,39,158","sellPrice3":"-","sellPrice4":"-","sellPrice5":"-","change":"-5.35","surv_indicator":"-","ndStartDate":"-","buyQuantity4":"-","isExDateFlag":"false","buyQuantity3":"-","buyQuantity2":"-","buyQuantity1":"-","series":"EQ","faceValue":"10.00","buyQuantity5":"-","closePrice":"0.00","open":"520.00","isinCode":"INE081A01012","lastPrice":"514.00"}],"optLink":"\/marketinfo\/sym_map\/symbolMapping.jsp?symbol=TATASTEEL&amp;instrument=-&amp;date=-&amp;segmentLink=17&amp;symbolCount=2","otherSeries":["EQ","E1"],"futLink":"\/live_market\/dynaContent\/live_watch\/get_quote\/GetQuoteFO.jsp?underlying=TATASTEEL&amp;instrument=FUTSTK&amp;expiry=28MAR2019&amp;type=-&amp;strike=-","lastUpdateTime":"27-MAR-2019 15:59:59"}
b=pd.DataFrame.from_dict(a,orient='index').transpose()
#print(type(b.data))

c=pd.Series([b.data]).values
print(b['data'].loc['symbol':].values)
d=b.data.values
print(d.shape)
for aa in d:
  ab=aa
  print(type(ab))
  print(ab[0])
  ana=dict(ab[0])
  print(type(ana))
  print(ana["symbol"])
  print(ana["totalSellQuantity"])
