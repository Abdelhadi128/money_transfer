# import mysql.connector as sql
# import json as j

# with open('data_coins.json','r') as json_fil :
#     all_data = j.loads(json_fil.read())
# all_keys = all_data.keys()
# data_base = sql.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
#     database = "mony_transfer"
# )
# for k in all_keys :
#     # date = k
#     for coin in all_data[k] :
#         mycursor = data_base.cursor()
 
#         mysql = 'INSERT INTO coins_values (date,coin_name,coin_price) VALUES (%s,%s,%s)'
#         val = (k , coin , all_data[k][coin])
#         mycursor.execute(mysql , val)
# data_base.commit()


import mysql.connector as sql
import json as j
import requests as r

with open('data_coins.json','r') as json_fil :
    all_data = j.loads(json_fil.read())
    
all_keys = all_data.keys()
data_base = sql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mony_transfer"
)
enline_coins = r.get('https://api.currencyfreaks.com/v2.0/rates/latest?apikey=d84d067c7f85429e91d5982de00fbcd4')
enline_coins_value = j.loads(enline_coins.text)
date = enline_coins_value['date'][0:10]
coins_names = enline_coins_value['rates'].keys()
for coin in coins_names :
    mycursor = data_base.cursor()
    mysql = 'INSERT INTO coins_values (date,coin_name,coin_price) VALUES (%s,%s,%s)'
    val = (date , coin , enline_coins_value['rates'][coin])
    mycursor.execute(mysql , val)
data_base.commit()