
import streamlit as st 
import json as j
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px 
from datetime import date

with open('Coins.txt','r') as coins_names:
    l_coins = [line.strip() for line in coins_names]

with open('data_coins.json','r') as old_data_coins:
    old_data_coins_v = j.loads(old_data_coins.read())
# l_date = old_data_coins_v.keys()
# print(old_data_coins_v.keys())
dates = list(old_data_coins_v.keys())[::-1]

st.title (':green[Currency Converter]')
container = st.form(key='Currency Converter')
col1,col2,col3 = container.columns([2,0.3,2])
option1 = col1.selectbox("From currency of", l_coins, index=None)
col2.form_submit_button('→\n\n←')
option2 = col3.selectbox("To currency of", l_coins, index=None)
col4 , col5 = container.columns([2,2])
amount = col4.number_input('Amount',value=1.00)
old_d = col5.selectbox("Date", dates, placeholder='Choose a date', index=None)

def transfére(coin1, coin2, amount):
    if coin1 and coin2:
        try:
            if old_d:
                coin11 = float(old_data_coins_v[old_d][coin1])
                coin22 = float(old_data_coins_v[old_d][coin2])
            else:
                today = str(date.today())
                coin11 = float(old_data_coins_v[today][coin1])
                coin22 = float(old_data_coins_v[today][coin2])

            result = coin22 / coin11 * amount
            container.info(f'{amount} {coin1} = {round(result, 4)} {coin2}')
        except (KeyError, ValueError):
            container.error('Invalid data for conversion.')
            st.stop()
    else:
        container.error('You have to choose two currencies')
        st.stop()

if container.form_submit_button('transformation', type='primary'):
    transfére(option1, option2, amount)
