import streamlit as st
import pickle
import numpy as np

st.title('Phone Price Prediction')

st.write('How many RAM ')
ram = st.text_input(label = 'Range from 256 to 4000',  value = 3000, key = '1')

st.write('What\'s the battery capacity')
battery_power = st.text_input(label = 'Range from 500 to 2000',  value = 1000,key = '2')

st.write('What\'s the pixel height')
px_height = st.text_input(label = 'Range from 500 to 2000',  value = 1000,key = '3')

st.write('What\'s the pixel width')
px_width = st.text_input(label = 'Range from 500 to 2000',  value = 1000,key = '4')

click = st.button('Predict')
if click:
    with open('Final_model.pkl', mode = 'rb') as pickle_in:
        pipe = pickle.load(pickle_in)
    input_val = [ram,battery_power,px_height,px_width]
    input_val = np.reshape(input_val,(1,-1))
    predict = pipe.predict(input_val)

    st.write(f'Your price range is {predict[0]}')
    dict = {0:'low cost',
            1:'medium cost',
            2:'high cost',
            3:'very high cost'}
    st.write(f'The phone you picked will be {dict[predict[0]]}.')
