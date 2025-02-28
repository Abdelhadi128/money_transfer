
import streamlit as st
import json as j
import numpy as np
import pandas as pd
from datetime import date

# Load currency names from premium_coins.txt
premium_coins_path = r'C:\Users\abdel\OneDrive\Documents\money_transfer\pages\premium_coins.txt'
try:
    with open(premium_coins_path, 'r') as coins_file:
        l_coins = [line.strip() for line in coins_file]
except FileNotFoundError:
    st.error(f"File not found: {premium_coins_path}")
    st.stop()

# Load historical exchange rates from data_coins.json
try:
    with open('data_coins.json', 'r') as old_data_coins:
        old_data_coins_v = j.load(old_data_coins)
except FileNotFoundError:
    st.error("File not found: data_coins.json")
    st.stop()
except j.JSONDecodeError:
    st.error("Error reading data_coins.json. Ensure it's a valid JSON file.")
    st.stop()

# Extract dates and reverse order for selection
dates = list(old_data_coins_v.keys())[::-1]

# Display title with red color
st.markdown("<h1 style='color: red;'>Currency Converter</h1>", unsafe_allow_html=True)

container = st.form(key='Currency Converter')

# Currency selection UI
col1, col2, col3 = container.columns([2, 0.3, 2])
option1 = col1.selectbox("From currency of", l_coins, index=None)
col2.form_submit_button('→\n\n←')
option2 = col3.selectbox("To currency of", l_coins, index=None)

col4, col5 = container.columns([2, 2])
amount = col4.number_input('Amount', value=1.00)
old_d = col5.selectbox("Date", dates, placeholder='Choose a date', index=None)

def transfére(coin1, coin2, amount):
    if coin1 and coin2:
        try:
            # Get exchange rates for the selected date or fallback to today
            selected_date = old_d if old_d else str(date.today())

            if selected_date not in old_data_coins_v:
                container.error(f"No data available for {selected_date}")
                return

            coin11 = float(old_data_coins_v[selected_date].get(coin1, 0))
            coin22 = float(old_data_coins_v[selected_date].get(coin2, 0))

            if coin11 == 0 or coin22 == 0:
                container.error('Invalid exchange rate data.')
                return

            result = (coin22 / coin11) * amount
            container.info(f'{amount} {coin1} = {round(result, 4)} {coin2}')

        except (KeyError, ValueError):
            container.error('Invalid data for conversion.')

if container.form_submit_button('transformation', type='primary'):
    transfére(option1, option2, amount)
