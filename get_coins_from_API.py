import requests as r
import json as j

with open('data_coins.json', 'r') as file:
    data = j.loads(file.read())
# Modify the JSON data
enline_coins = r.get('https://api.currencyfreaks.com/v2.0/rates/latest?apikey=331c923ced78485fa86dc056ab62652d')
enline_coins_value = j.loads(enline_coins.text)['rates']
# print(enline_coins_value)
date = {j.loads(enline_coins.text)['date'][0:10]  : enline_coins_value}
data.update(date)
# print(date)

# Write the updated JSON data back to the file
with open('data_coins.json', 'w') as file:
    j.dump(data, file, indent=2)