from populate import base
from dbconn.models import *
from multiprocessing import Pool
import multiprocessing
import pandas
import time
"""
#DBs='db.sqlite3'
currencys=['SEK','NZD','THB','PHP','IDR','EUR','KRW'\
,'VND','MYR','CNY']
"""
currencys=[
'USD','HKD','GBP','AUD','CAD','SGD','CHF','JPY'\
,'ZAR','SEK','NZD','THB','PHP','IDR','EUR','KRW'\
,'VND','MYR','CNY'
]

objcurrencys={
'USD':USDCurrency,'HKD':HKDCurrency,'GBP':GBPCurrency,'AUD':AUDCurrency,
'CAD':CADCurrency,'SGD':SGDCurrency,'CHF':CHFCurrency,'JPY':JPYCurrency,
'ZAR':ZARCurrency,'SEK':SEKCurrency,'NZD':NZDCurrency,'THB':THBCurrency,
'PHP':PHPCurrency,'IDR':IDRCurrency,'EUR':EURCurrency,'KRW':KRWCurrency,
'VND':VNDCurrency,'MYR':MYRCurrency,'CNY':CNYCurrency
}
def addcurrency(currency):
    #USDCurrency.objects.all().delete()
    #dfcurrencys = pandas.DataFrame()
    datetime = time.strftime("%Y/%m",time.localtime())#格式：2017/10
    #for currency in currencys:
    dfcurrencys = pandas.DataFrame()
    print ('幣別:'+currency+'開始時間:'+time.asctime( time.localtime() ))
    result = pandas.date_range(datetime, periods=1, freq='M')#pandas自動產生日期
    #result = pandas.date_range('2008/06', periods=204, freq='M')
    #result = pandas.date_range('2016/01', periods=36, freq='M')
    for dt in result:
        formatdate=str(dt.to_pydatetime()).split('-')
        Date=formatdate[0]+'-'+formatdate[1]
        url ='http://rate.bot.com.tw/xrt/quote/'+Date+'/'+currency
        dfs = pandas.read_html(url)
        dfcurrency = dfs[0]

        if dfcurrency.empty!=True:
            dfcurrency = dfcurrency.iloc[:,0:6]
            dfcurrency.columns=['date','currency','Cashbuying', 'Cashselling', 'Spotbuying', 'Spotselling']
            dfcurrency =dfcurrency.drop(['currency'],axis = 1)
            dfcurrencys = dfcurrencys.append(dfcurrency)
            #print(dfcurrencys)
        #time.sleep(2)
        add_db(dfcurrencys, currency)

        #for dc in dfcurrency.to_records(index=False):
        #    usdcurrency=USDCurrency()
        #    if USDCurrency.objects.filter(date=dc[0]).exists()==False:#查詢匯率資料是否存在，不存在則新增
        #        usdcurrency.date=dc[0]
        #        usdcurrency.CashBuying=round(float(dc[1]),3)
        #        usdcurrency.CashSelling=round(float(dc[2]),3)
        #        usdcurrency.SpotBuying=round(float(dc[3]),3)
        #        usdcurrency.SpotSelling=round(float(dc[4]),3)
        #        usdcurrency.save()
        #        print(usdcurrency.date+' '+str(usdcurrency.CashBuying)+' '+str(usdcurrency.CashSelling)+' '
        #            +str(usdcurrency.SpotBuying)+' '+str(usdcurrency.SpotSelling)+':DONE')
        
                    
    print ('幣別:'+currency+'結束時間:'+time.asctime( time.localtime(time.time()) ))

def add_db(dfcurrencys, currency):
    for dc in dfcurrencys.to_records(index=False):
        dbcurrency=chk_currency(currency)()
        if chk_currency(currency).objects.filter(date=dc[0]).exists()==False:#查詢匯率資料是否存在，不存在則新增
            
            dbcurrency.date=dc[0]
            dbcurrency.CashBuying=round(float(str(dc[1]).replace('-','0.0')),5)
            dbcurrency.CashSelling=round(float(str(dc[2]).replace('-','0.0')),5)
            dbcurrency.SpotBuying=round(float(str(dc[3]).replace('-','0.0')),5)
            dbcurrency.SpotSelling=round(float(str(dc[4]).replace('-','0.0')),5)
            dbcurrency.save()
            print(dbcurrency.date+' '+str(dbcurrency.CashBuying)+' '+str(dbcurrency.CashSelling)+' '
                +str(dbcurrency.SpotBuying)+' '+str(dbcurrency.SpotSelling)+':DONE')
            

def chk_currency(currency):
    if objcurrencys.__contains__(currency):
        return objcurrencys.get(currency)

if __name__ == '__main__':
    tStart = time.time()#計時開始
    print ('addcurrency()')
    pool = Pool(multiprocessing.cpu_count())
    result1 = pool.map(addcurrency, currencys, chunksize=5)#單一參數
    #result1 = pool.starmap(addrate, zip(arguments_list1, date_range), chunksize=4)#多參數
    pool.close()
    pool.join()
    tEnd = time.time()#計時結束
#列印結果
    print ("It cost %f sec" % (tEnd - tStart))#自動進位
    print (tEnd - tStart)#原型
    #addcurrency()