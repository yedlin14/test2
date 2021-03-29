from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
import json
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://yavuz-dc:mongodeepcase2021@cluster0.jiprv.mongodb.net/test?retryWrites=true&w=majority")
mydb = cluster["test"]
collections =mydb["test"]

otx = OTXv2("00dddd47499d5f3f0d1152e3f987569700260c64a4185be0153092f7f86645e7")
# Get all the indicators associated with a pulse

indicators = otx.get_indicator_details_by_section(IndicatorTypes.IPv4, "23.227.38.32", 'general')
#indicators = otx.get_indicator_details_by_section(IndicatorTypes.IPv4, "23.227.38.32", 'general')
#collections.insert_one(indicators['country_name'])

data = {}
data['ip'] = indicators['indicator']
data['asn'] = indicators['asn']
data['country'] = indicators['country_name']


print(data)
'''
for indicator in indicators:
#     # coprint(indicator + " - " + indicator.)

    print(indicator,';',indicators[indicator])
#    with open('ip_ailen_voult.json', 'w') as outfile:
#        json.dump((indicator,';',indicators[indicator]), outfile)
#     for section in indicators['sections']:
#         print(section,';',section[ section])

    # Get everythinfsg OTX knows about google.com
#print(json.dumps(indicators, indent=4))


#indicators = otx.get_pulse_indicators("5fef5b647be6e406857e1b59")

#for indicator in indicators:
 #   print(indicator + indicator['type'])
# Get everything OTX knows about google.com


otx.get_indicator_details_full(IndicatorTypes.DOMAIN, "google.com")






#Open the atlas-starter.py file. On line 8, replace the placeholder text with the connection string to your Atlas cluster.

#client = pymongo.MongoClient("mongodb+srv://yavuz-dc:<password>@cluster0.jiprv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

'''


deneme=otx.get_indicator_details_by_section(IndicatorTypes.IPv4, "23.227.38.32", 'passive_dns')
print(deneme)

for x in range(500):
    data2['passive_dns'] =(passive_dns['passive_dns'][x]['last'])
    data2['passive_dns']['hostname'] =(passive_dns['passive_dns'][x]['hostname'])
    data2['passive_dns']['record_type'] =(passive_dns['passive_dns'][x]['record_type'])
    data2['passive_dns']['indicator_link'] =(passive_dns['passive_dns'][x]['indicator_link'])
    data2['passive_dns']['flag_title'] =(passive_dns['passive_dns'][x]['flag_title'])
    data2['passive_dns']['asset_type'] =(passive_dns['passive_dns'][x]['asset_type'])
    data2['passive_dns']['asn'] =(passive_dns['passive_dns'][x]['asn'])
