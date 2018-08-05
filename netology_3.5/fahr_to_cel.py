import requests

import xml.etree.cElementTree as ET

# import osa

def fahr_to_cel(fahr):
    headers = {"Content-Type": "text/xml"}
    data = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <FahrenheitToCelsius xmlns="https://www.w3schools.com/xml/">
      <Fahrenheit>{fahr}</Fahrenheit>
    </FahrenheitToCelsius>
  </soap:Body>
</soap:Envelope>"""

    res = requests.post("https://www.w3schools.com/xml/tempconvert.asmx", data=data, headers=headers)

    root = ET.fromstring(res.text)

    return root[0][0][0].text

# client = osa.Client("https://www.w3schools.com/xml/tempconvert.asmx?WSDL") # Не получилось c:
# print(client.service.FahrenheitToCelsius("10"))


path = input("path to file:")

x = 0
with open(path, "r") as f:
    data = f.readlines()
    sum = 0
    for i in data:
        i = i.replace(" F", "")
        sum += int(i)
    x = sum/len(data)

result = fahr_to_cel(x)
print(result, " C")