from populate import base
from bs4 import BeautifulSoup
import requests
import sys
import re
from dbconn.models import Invoices
#import sqlite3
#conn = sqlite3.connect('resoucedata.sqlite3')
def addinvoice1():#歷史資料
    url ='https://bluezz.com.tw/invoice_history.php'
    html = requests.get(url).text
    sp = BeautifulSoup(html, 'html.parser')
    all_data = sp.find_all(style=re.compile("text-align:left"))#找出html內style=text=align:left的資料
    rows = all_data[0].find_all('div')
    all_nums = []
    item= []
    i=0
    for row in rows:
        if i!=0 and i%7==0:
            all_nums.append(item[0:6])
            item.clear()
        item.append(row.string)
        i+=1
    for num in all_nums:
        date = str(num[0])
        special=num[1].split(":")#文字與數字分開
        one=num[2].split(":")#文字與數字分開
        head=num[3].split(":")#文字與數字分開
        six=num[4].split(":")#文字與數字分開
        duijiang =num[5]
        #print(date)
        if len(date)<9:
            date = date[0:3]+'年'+'0'+date[4:5]+'、'+'0'+date[6:7]+'月'
        if len(date)<10:
            date=  date[0:3]+'年'+'0'+date[4:5]+'、'+date[6:8]+'月'
        add_db(date, special[1], one[1], head[1], six[1], duijiang)
        #if len(cursor.fetchall()) == 0:
        #    sqlstr = "insert into invoice values('{}', '{}', '{}', '{}', '{}', '{}');".format(num[0], special[1], one[1], head[1], six[1], num[5])
            #Date,special,one,head,six,兌獎日
        #    print(sqlstr)
def addinvoice2():
    import pandas as pd
    from bs4 import BeautifulSoup
    import requests
    import urllib.request
    import numpy as np
    url ='http://invoice.etax.nat.gov.tw/'
    invoices=pd.read_html(url)[0:2]
    invoices
    page = urllib.request.urlopen(url)
    html= page.read()
    sp = BeautifulSoup(html, 'html.parser')
    date = sp.find_all("h2")
    duijiang = sp.select("p.date")
    
    duijiang=duijiang[0].text.replace('領獎期間自','兌獎日期:').replace('年','-').replace('月','-').replace('日起至','~ ').replace('日止','')
    print(duijiang)
    newdate=date[1].text#最新一期的日期
    olddate=date[3].text#上一期的日期
    #invoices[0]
    newinvoice = invoices[0].drop([4,5,6,7,8]).pop(1)#去掉4,5,6,7,8列
    oldinvoice = invoices[1].drop([4,5,6,7,8]).pop(1)
    #print(newinvoice)
    #print(oldinvoice)
    c =[]
    d =[]
    for n in newinvoice:
        b=n.split(" ")
        c.append(b[0])
    for o in oldinvoice:
        b=o.split(" ")
        d.append(b[0])
    c[0]=newdate.replace('-','、')
    d[0]=olddate.replace('-','、')
    add_db(c[0], c[1], c[2], c[3], c[4], duijiang)

def add_db(date, special, one, head, six, duijiang):
    if Invoices.objects.filter(date=date).exists() == False:
        print('add DB......')
        db=Invoices()
        db.date=date
        db.special=special
        db.one=one
        db.head=head
        db.six=six
        db.duijiang=duijiang
        db.save()

if __name__ == '__main__':
    addinvoice1()
    addinvoice2()
        