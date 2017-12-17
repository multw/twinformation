from populate import base
import requests
import pandas as pd
from dbconn.models import Rate
from datetime import datetime, time
def addratechange():
	currencylist=['USDTWD','USDCNY','USDHKD','USDJPY','USDEUR',
	              'USDGBP','USDAUD','USDCAD','USDSGD','USDCHF',
	              'USDNZD','USDTHB','USDPHP','USDIDR','USDVND',
	              'USDKRW','USDMYR','USDUSD']
	r=requests.get('https://tw.rter.info/capi.php')
	currency=r.json()
	#print(currency)
	currencydict=dict.fromkeys(currencylist)
	for i in currencylist:
		if i == 'USDUSD':
			currencydict[i]=currency[i[3:6]]
		currencydict[i]=currency[i]
	dfc = pd.DataFrame(currencydict)
	
#####json新增到db
	#print(dfc.to_json())
	rate = Rate()
	rate.date = datetime.now()
	rate.jsondata = dfc.to_json()
	rate.save()
#####json新增到db

	#dfc.to_json('./dbconn/rate.json')

if __name__ == '__main__':
    print ('addratechange()')
    addratechange()