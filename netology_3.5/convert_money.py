import requests

import xml.etree.cElementTree as ET

from pprint import pprint

def convert_to_rub(cur_from, value,cur_to="RUB"):
    headers = {"Content-Type": "text/xml"}
    data = f"""<?xml version="1.0" encoding="utf-8"?> 
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
        xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
        xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"> 
        <soap:Body> 
            <Convert xmlns="http://webservices.currencysystem.com/currencyserver/">
                <licenseKey>{""}</licenseKey> 
                <fromCurrency>{cur_from}</fromCurrency> 
                <toCurrency>{cur_to}</toCurrency> 
                <amount>{value}</amount> 
                <rounding>{"false"}</rounding> 
                <format>{""}</format> 
                <returnRate>{"curncsrvReturnRateNumber"}</returnRate> 
                <time>{""}</time> 
                <type>{""}</type> 
            </Convert> 
        </soap:Body> 
    </soap:Envelope>"""

    res = requests.post("https://fx.currencysystem.com/webservices/CurrencyServer5.asmx", data=data, headers=headers)

    root = ET.fromstring(res.text)

    return root[0][0][0].text, cur_to # Немного апдейтнул. Теперь выводит еще валюту, в которую надо перевести с:


path = input("path to file:")

with open(path, "r") as f:
    data = f.readlines()
    for i in data:
        data_list = i.split(" ")
        data_list[2] = data_list[2].replace("\n", "")
        res, lang = convert_to_rub(data_list[2], data_list[1])
        print(data_list[0] + " " + res + " " + lang)
