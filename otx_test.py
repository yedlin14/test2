from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
import json
import pymongo
from pymongo import MongoClient

# Mongo için bağlantı
cluster = MongoClient("mongodb+srv://yavuz-dc:mongodeepcase2021@cluster0.jiprv.mongodb.net/test?retryWrites=true&w=majority")
mydb = cluster["test"]
collections =mydb["test"]

#   otx için Api Key
otx = OTXv2("00dddd47499d5f3f0d1152e3f987569700260c64a4185be0153092f7f86645e7")


#   Otx ile genel sorgu
indicators = otx.get_indicator_details_by_section(IndicatorTypes.IPv4, "23.227.38.32", 'general')

#   Otx ile Passive DNS Sorgusu
passive_dns = otx.get_indicator_details_by_section(IndicatorTypes.IPv4, "23.227.38.32", 'passive_dns')

# Gelen sorguyu istediğimiz formata göre ayarlama
data = {}
data2 = {}
data['ip'] = indicators['indicator']
data['asn'] = indicators['asn']
data['country'] = indicators['country_name']
data['passive_dns'] = passive_dns['passive_dns']



print(data)

#   Veri tabanına yazma 
collections.insert_one(data)

