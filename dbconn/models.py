from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
# Create your models here.

class Invoices(models.Model):
	date = models.CharField(max_length=40)
	special = models.CharField(max_length=40)
	one = models.CharField(max_length=40)
	head = models.CharField(max_length=40)
	six = models.CharField(max_length=40)
	duijiang = models.CharField(max_length=40)

class Post(models.Model):
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('-pub_date',)

	def __str__(self):
		return self.title

class USDCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

	def __str__(self):
		return self.date

class OilPrice(models.Model):
	odate = models.DateField()
	o92 = models.DecimalField(max_digits=3, decimal_places = 1, blank=True, null=True)
	o95 = models.DecimalField(max_digits=3, decimal_places = 1, blank=True, null=True)
	o98 = models.DecimalField(max_digits=3, decimal_places = 1, blank=True, null=True)
	ohigh = models.DecimalField(max_digits=3, decimal_places = 1, blank=True, null=True)

	class Meta:
		ordering = ('-odate',)

class Rate(models.Model):
	date = models.CharField(max_length=40)
	jsondata = JSONField()

	class Meta:
		ordering = ('-date',)

	def __str__(self):
		return self.date

class HKDCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class GBPCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class AUDCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class CADCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class SGDCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class CHFCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class JPYCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class ZARCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class SEKCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class NZDCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class THBCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class PHPCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class IDRCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class EURCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class KRWCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class VNDCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class MYRCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class CNYCurrency(models.Model):
	date = models.CharField(max_length=200)
	CashBuying = models.FloatField()
	CashSelling= models.FloatField()
	SpotBuying= models.FloatField()
	SpotSelling= models.FloatField()

	class Meta:
		ordering = ('-date',)

class CurrencyCode(models.Model):
	code = models.CharField(max_length=20)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.code