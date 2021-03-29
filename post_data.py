import requests
from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
import json
import base64
import os, sys



response = requests.get('http://127.0.0.1:8080/api/receive')
ip = response.json()


otx = OTXv2("00dddd47499d5f3f0d1152e3f987569700260c64a4185be0153092f7f86645e7")

indicators = otx.get_indicator_details_by_section(IndicatorTypes.IPv4, ip, 'general')
passive_dns = otx.get_indicator_details_by_section(IndicatorTypes.IPv4, "23.227.38.32", 'passive_dns')


data = {}
data2 = {}
data['ip'] = indicators['indicator']
data['asn'] = indicators['asn']
data['country'] = indicators['country_name']
data['passive_dns'] = passive_dns['passive_dns']
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

url='http://127.0.0.1:8080/api/upload'

requests.post(url, data=json.dumps(data))


