from django import forms
from .models import *
import pandas as pd

objcurrencys={
'USD':USDCurrency,'HKD':HKDCurrency,'GBP':GBPCurrency,'AUD':AUDCurrency,
'CAD':CADCurrency,'SGD':SGDCurrency,'CHF':CHFCurrency,'JPY':JPYCurrency,
'ZAR':ZARCurrency,'SEK':SEKCurrency,'NZD':NZDCurrency,'THB':THBCurrency,
'PHP':PHPCurrency,'IDR':IDRCurrency,'EUR':EURCurrency,'KRW':KRWCurrency,
'VND':VNDCurrency,'MYR':MYRCurrency,'CNY':CNYCurrency
}

class InvoiceForm(forms.Form):
	invoice = Invoices.objects.all().order_by('-date')
	id=[]
	for i in invoice:
		id.append([i.id,i.date])#<option value=i.id>i.date</option>
		#print(id)
	user_date = forms.ChoiceField(label='選擇開獎日期', choices=id, widget=forms.Select(
		attrs={'onchange': 'this.form.submit();','class': 'form-control'}))

class oilForm(forms.Form):
	oilprice = OilPrice.objects.all().order_by('-odate')
	date=[]
	years=[['請選擇','請選擇']]
	for o in oilprice:
		date.append(o.odate)
	for i in date:
		if [i.year,i.year] not in years:
			#print(i.year)
			years.append([i.year,i.year])
	#for y in years:
		#print(y)
	oil_date = forms.ChoiceField(label='選擇查詢年份', choices=years, widget=forms.Select(
		attrs={'onchange': 'this.form.submit();','class': 'form-control'}))

class currencyForm(forms.Form):
	def __init__(self, currency, *args, **kwargs):
		super(currencyForm, self).__init__(*args, **kwargs)
		self.fields['currency_date'].choices = currency
	"""		
	#去除
	currencys = USDCurrency.objects.all().order_by('-date')
	year=[]
	years=[['請選擇','請選擇']]
	for u in currencys:
		#print(u.date)
		year, month, day = u.date.split('/')
		#print(year)
		#year.append(year)
		if [year,year] not in years:
			print(year)
			years.append([year,year])
	print(years)
	#去除
	"""
	currency_date = forms.ChoiceField(label='選擇查詢年份', choices=(), widget=forms.Select(
		attrs={'onchange': 'this.form.submit();','class': 'form-control'}))
	#return currency_date

class RateCurrencyForm(forms.Form):
	rate = Rate.objects.all().order_by('-date')[:1]
	for r in rate:
		json = r.jsondata
	#print(json)
	dfcurrency=pd.read_json(json)
	#print(dfcurrency)
	currencylist=[]
	for c in dfcurrency.keys():#所有幣別
	    currencylist.append([c[3:6],c[3:6]])
	
	source = forms.ChoiceField(label='選擇幣別', choices=currencylist, widget=forms.Select(
		attrs={'class': 'form-control'}))
	destination = forms.ChoiceField(label='選擇幣別', choices=currencylist, widget=forms.Select(
		attrs={'class': 'form-control'}))
	coins = forms.CharField(label='輸入兌換金額', max_length=10, widget=forms.TextInput(
		attrs={'type':'number','class': 'form-control'}))

	def get_update_time():
		rate = Rate.objects.all().order_by('-date')[:1]
		for r in rate:
			json = r.jsondata
		#json='./dbconn/rate.json'
		dfcurrency=pd.read_json(json)
		#print(dfcurrency)
		currencylist=[]
		update=[]
		for key,value in dfcurrency.items():
			currencylist.append(key[3:6])
		updatedict=dict.fromkeys(currencylist)
		for i in currencylist:
			updatedict[i]=dfcurrency['USD'+i]['UTC']
		#print(updatedict)
		return updatedict

