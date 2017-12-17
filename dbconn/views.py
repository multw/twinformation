from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from django.core.paginator import Paginator,Page,PageNotAnInteger,EmptyPage
from .models import *
from datetime import datetime, time
from dbconn import forms, ratechange
import math, json
import requests
import pandas as pd
import pytz


# Create your views here.

objcurrencys={
'USD':USDCurrency,'HKD':HKDCurrency,'GBP':GBPCurrency,'AUD':AUDCurrency,
'CAD':CADCurrency,'SGD':SGDCurrency,'CHF':CHFCurrency,'JPY':JPYCurrency,
'ZAR':ZARCurrency,'SEK':SEKCurrency,'NZD':NZDCurrency,'THB':THBCurrency,
'PHP':PHPCurrency,'IDR':IDRCurrency,'EUR':EURCurrency,'KRW':KRWCurrency,
'VND':VNDCurrency,'MYR':MYRCurrency,'CNY':CNYCurrency
}

def homepage(request):
	template = get_template('index.html')

	posts = Post.objects.all()
	now = datetime.now()
	html = template.render(locals())
	#post_lists = list()
	#for count, post in enumerate(posts):
	#	post_lists.append("No.{}:".format(str(count))+str(post)+"<hr>")
	#	post_lists.append("<small>"+str(post.body)\
	#		+"</small><br><br>")
	return HttpResponse(html)

def showpost(request, slug):
	template = get_template('post.html')
	try:
		post = Post.objects.get(slug=slug)
		if post != None:
			html = template.render(locals())#用locals()把所有區域變數使用字典型態打包。
			return HttpResponse(html)
	except:
		return redirect('/')

def USD(request, currency):
	template = get_template('currency.html')
	date=[]
	Cashbuying=[]
	Cashselling=[]
	Spotbuying=[]
	Spotselling=[]
	currency_title = CurrencyCode.objects.filter(code__contains=currency)
	#print(currency_title)
	for c in currency_title:
		title=c.name
	try:#選擇年份
		currency_date = request.GET['currency_date']
		currencylist = chk_currency(currency).objects.filter(date__contains=currency_date).order_by('-date')
		usdcurrencycharts = chk_currency(currency).objects.filter(date__contains=currency_date).order_by('date')#for charts用
		paginator=Paginator(currencylist,20,orphans=4)
		range=paginator.page_range
	except:#無資料，取最新一筆匯率
		currency_date = None
		currencylist = chk_currency(currency).objects.all().order_by('-date')[:1]#負的表示降冪排列，最新一筆
		usdcurrencycharts = chk_currency(currency).objects.order_by('-date')[:10]#for charts用
		usdcurrencycharts = reversed(usdcurrencycharts)#內建函數reversed()，反轉參數 (parameter) seq 中元素的順序
		paginator=Paginator(currencylist,20)#分頁
	#print(curr.date)
	#for u in usdcurrencylist:
	#print(sorted(usdcurrencycharts))
	
	try:#分頁
		choise_page=request.GET.get('page')
		result=paginator.page(choise_page)
	except PageNotAnInteger as e:
		result=paginator.page(1)
	except EmptyPage as e:
		result=paginator.page(1)	
	for u in usdcurrencycharts:
		#print(u.date)
		date.append(u.date)
		Cashbuying.append(u.CashBuying)
		Cashselling.append(u.CashSelling)
		Spotbuying.append(u.SpotBuying)
		Spotselling.append(u.SpotSelling)
	#print(Cashselling)
	json_date = json.dumps(date)
	years = data_years(currency)#產生choicefield的值
	currencyform = forms.currencyForm(years)
	#print(currencyform)
	html = template.render(locals())
	return HttpResponse(html)

def Oilprice(request):
	#print('Oilprice')
	template = get_template('oilprice.html')
	oilprice = OilPrice.objects.all().order_by('-odate')
	try:
		oil_date= request.GET['oil_date']
		print(oil_date)
		oilpricelist = OilPrice.objects.filter(odate__contains=oil_date).exclude(o92='NaN',o95='NaN',o98='NaN',ohigh='NaN').order_by('-odate')
		print(oilpricelist)
		for o in oilpricelist:
			if math.isnan(o.o92):
				o.o92='無調整'
			if math.isnan(o.o95):
				o.o95='無調整'
			if math.isnan(o.o98):
				o.o98='無調整'
			if math.isnan(o.ohigh):
				o.ohigh='無調整'
		paginator=Paginator(oilpricelist,10,orphans=4)
		range=paginator.page_range
		print(range)
	except:
		oil_date = None
		print('except')
		oilpricelist = OilPrice.objects.all().exclude(o92='NaN',o95='NaN',o98='NaN',ohigh='NaN').order_by('-odate')[:1]
		paginator=Paginator(oilpricelist,20,orphans=4)
	#if oil_date != None:
	try:
		choise_page=request.GET.get('page')
		result=paginator.page(choise_page)
	except PageNotAnInteger as e:
		result=paginator.page(1)
	except EmptyPage as e:
		result=paginator.page(1)
	print(type(oil_date))
	oilform = forms.oilForm()
	html = template.render(locals())
	return HttpResponse(html)

def Invoice(request):
	if request.method == 'GET':#初始顯示最新一期發票開獎號
		print('#######GET_method#######')
		invoicelist = Invoices.objects.all().order_by('-date')
		date = invoicelist[0].date
		special = invoicelist[0].special
		one = invoicelist[0].one
		head=invoicelist[0].head.split("、")
		six=invoicelist[0].six.split("、")
		iform = forms.InvoiceForm()
		#print(invoicelist)
	else:
		print('#######POST_method#######')
		iform = forms.InvoiceForm(request.POST)
		if iform.is_valid():
			user_date = iform.cleaned_data['user_date']
		invoicelist = Invoices.objects.get(id=user_date)
		date = invoicelist.date
		special = invoicelist.special
		one = invoicelist.one
		head=invoicelist.head.split("、")
		six=invoicelist.six.split("、")
	template = get_template('invoice.html')
	#request_context = RequestContext(request)
	#request_context.push(locals())
	html = template.render(context=locals(),request=request)
	return HttpResponse(html)

def Rate(request):
	updatetime=forms.RateCurrencyForm.get_update_time()
	print(updatetime)
	us = pytz.timezone('US/Pacific')
	if request.method == 'GET':
		rateform=forms.RateCurrencyForm()
	else:
		rateform=forms.RateCurrencyForm(request.POST)
		if rateform.is_valid():
			source = rateform.cleaned_data['source']
			destination = rateform.cleaned_data['destination']
			coins = rateform.cleaned_data['coins']
			times=updatetime[source]
			utc_time=datetime.strptime(times,"%Y-%m-%d %H:%M:%S").replace(tzinfo=us)
			#print(utc_time)
			localtime=utc_time.astimezone(pytz.utc)
			print(localtime.time())
			print(localtime.date())

		rate= ratechange.SourceToDestination( source, destination, coins)


	template = get_template('rate.html')
	#print(locals())
	html = template.render(context=locals(),request=request)
	return HttpResponse(html)

def chk_currency(currency):
    if objcurrencys.__contains__(currency):
        return objcurrencys.get(currency)

def data_years(currency):
	currencys = chk_currency(currency).objects.all().order_by('-date')
	year=[]
	years=[['請選擇','請選擇']]
	for u in currencys:
		#print(u.date)
		year, month, day = u.date.split('/')
		#print(year)
		#year.append(year)
		if [year,year] not in years:
			#print(year)
			years.append([year,year])
	return years
