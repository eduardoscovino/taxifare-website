import streamlit as st

import datetime
import requests

'''
# NYC Taxifare Generator
'''

st.markdown('''
Welcome to the taxifare prediction.
            
Here you get the right price to go anywhere you want!
            
''')


with st.form(key='params_for_api'):

    pickup_date = st.date_input('Pickup date', value=datetime.date(2012, 10, 6))
    pickup_time = st.time_input('Pickup time', value=datetime.time(12, 10, 00))
    pickup_datetime = f'{pickup_date} {pickup_time}'
    pickup_longitude = st.number_input('Pickup longitude', value=40.7614327)
    pickup_latitude = st.number_input('Pickup latitude', value=-73.9798156)
    dropoff_longitude = st.number_input('Dropoff longitude', value=40.6413111)
    dropoff_latitude = st.number_input('Dropoff latitude', value=-73.7803331)
    passenger_count = st.number_input('Number of passengers', min_value=1, max_value=8, step=1, value=1)

    st.form_submit_button('Show me the price!')

params = dict(
    pickup_datetime=pickup_datetime,
    pickup_longitude=pickup_longitude,
    pickup_latitude=pickup_latitude,
    dropoff_longitude=dropoff_longitude,
    dropoff_latitude=dropoff_latitude,
    passenger_count=passenger_count
)

wagon_cab_api_url = 'https://taxifare-krterdwxrq-ew.a.run.app/predict'
response = requests.get(wagon_cab_api_url, params=params)

prediction = response.json()

pred = prediction['fare']

st.header(f'Fare amount: ${round(pred, 2)}')