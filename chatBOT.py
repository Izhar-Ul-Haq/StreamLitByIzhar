#import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly as pt
import streamlit as st
import sklearn as sk
import rasa as rs
#Created By Izhar Khan Khattak#
st.title("Izhar Khan Khattak")
st.header("This is just a dummy app")
st.header("Hi! we are gonna create ChatterBOT!")
st.video("https://youtu.be/yhQG8uIolX4")
st.image("https://media.licdn.com/dms/image/C4D03AQHMXbf3SYxLaw/profile-displayphoto-shrink_800_800/0/1647682327612?e=1676505600&v=beta&t=jPBfDVRbVkK1fGaSzq9j0CyZixmcFP_3AHjyQcRx9X4")
st.camera_input("Take a picture")
#Take inputs from the user
st.text_input('Please your first name')
# Display interactive widgets
st.button('Click me')
st.checkbox('I agree')
st.radio('Pick one', ['cats', 'dogs'])
st.selectbox('Pick one', ['cats', 'dogs'])
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.date_input('Your birthday')
st.time_input('Meeting time')
st.file_uploader('Upload a CSV')
# st.download_button('Download file', data)
st.color_picker('Pick a color')
print(rs.__version__)
print(rs)