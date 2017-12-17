from populate import base
import pandas
from dbconn.models import OilPrice
def addoil():
	dfs = pandas.read_html('http://new.cpc.com.tw/division/mb/oil-more4.aspx')
	#dfs[0]
	#table='oil'
	oil=dfs[0]
	oil=oil.ix[:,0:4]
	oil.columns=['odate','o92','o95','o98','ohigh']
	dfoil=oil.drop(0,axis = 0)#指定參數 axis = 0 表示要刪除觀測值（row），指定參數 axis = 1 表示要刪除欄位（column）
	#oil['odate']=dfoil['odate'].astype(str)
	#oil['o92']=dfoil['o92'].astype(float)
	#oil['o95']=dfoil['o95'].astype(float)
	#oil['o98']=dfoil['o98'].astype(float)
	#oil['ohigh']=dfoil['ohigh'].astype(float)
	print(dfoil)
	add_db(dfoil)

def add_db(dfoil):
	for o in dfoil.to_records(index=False):
		op=OilPrice()
		Date=o[0].replace('/','-')
		if OilPrice.objects.filter(odate=Date).exists() == False:
			#print(Date)
			op.odate=Date
			op.o92=round(float(o[1]),1)
			op.o95=round(float(o[2]),1)
			op.o98=round(float(o[3]),1)
			op.ohigh=round(float(o[4]),1)
			op.save()

if __name__ == '__main__':
    print ('addoil()')
    addoil()