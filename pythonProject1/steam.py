import json
import requests


dict = {}
errorList = []
params = {'appid' : 570, 'currency' : 1, 'market_hash_name' : 0}
with open('example.json', 'r+') as exmp:
    example = json.loads(exmp.read())
    for i in example['rgDescriptions']:
        if example['rgDescriptions'][i]['marketable'] == 1:
            params['market_hash_name'] = example['rgDescriptions'][i]['market_hash_name']
            resp = requests.get('http://steamcommunity.com/market/priceoverview/', params=params)
            respN = resp.json()
            if params['market_hash_name'] in dict.keys():
                dict[i]['quantity'] += 1
            else:
                try:
                    if respN['success']:
                        temp = {'success': respN['success'], 'lowest_price': respN['lowest_price'],
                                'median_price': respN['median_price'], 'quantity': 1}
                    if not respN['success']:
                        temp = {'success': respN['success'], 'quantity': 1}
                        errorList.append(i)
                    dict[i] = temp
                except:
                    temp = {'success': False, 'quantity': 1}
                    errorList.append(i)
                    dict[i] = temp


print(dict)
print(errorList)