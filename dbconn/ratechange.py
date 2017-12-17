import requests
import pandas as pd
#TWD$1000 -->JPY ex.SourceToDestination('TWD', 'JPY', 1000)
class SourceToDestination:
	def __init__(self,source,destination,coins):
		self.source = source
		self.destination = destination
		self.coins = coins

	def get_dollor(self):
		def OthertoUSD(source, coins):
			json='./dbconn/rate.json'
			currency=pd.read_json(json)
			toUSD='USD'+source
			return float(coins)/float(currency[toUSD]['Exrate'])

		def USDtoOther(source, coins):
			json='./dbconn/rate.json'
			currency=pd.read_json(json)
			toOther='USD'+source
			values=float(coins)*float(currency[toOther]['Exrate'])
			return values
		
		dollor=OthertoUSD(self.source, USDtoOther(self.destination,self.coins))
		return dollor
		
