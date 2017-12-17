from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'pub_date')
admin.site.register(Post, PostAdmin)

class USD(admin.ModelAdmin):
	list_display=('id','date','CashBuying', 'CashSelling', 'SpotBuying', 'SpotSelling')
admin.site.register(USDCurrency, USD)

class Oil(admin.ModelAdmin):
	list_display=('odate','o92','o95','o98','ohigh')
admin.site.register(OilPrice, Oil)

class CCode(admin.ModelAdmin):
	list_display=('code','name')
admin.site.register(CurrencyCode)

class Ratechange(admin.ModelAdmin):
	list_display=('date','jsondata')
admin.site.register(Rate, Ratechange)

class VND(admin.ModelAdmin):
	list_display=('id','date','CashBuying', 'CashSelling', 'SpotBuying', 'SpotSelling')
admin.site.register(VNDCurrency, VND)

class PHP(admin.ModelAdmin):
	list_display=('id','date','CashBuying', 'CashSelling', 'SpotBuying', 'SpotSelling')
admin.site.register(PHPCurrency, PHP)

class HKD(admin.ModelAdmin):
	list_display=('id','date','CashBuying', 'CashSelling', 'SpotBuying', 'SpotSelling')
admin.site.register(HKDCurrency, HKD)

class SEK(admin.ModelAdmin):
	list_display=('id','date','CashBuying', 'CashSelling', 'SpotBuying', 'SpotSelling')
admin.site.register(SEKCurrency, SEK)

class CHF(admin.ModelAdmin):
	list_display=('id','date','CashBuying', 'CashSelling', 'SpotBuying', 'SpotSelling')
admin.site.register(CHFCurrency, CHF)
