import pandas as pd
import plotly.express as px
import streamlit as st

# read data
car_data = pd.read_csv('vehicles.csv')

st.header('Car Sales Ads Distribution')

hist_button = st.button('Create Histogram')  # create a button

if hist_button:  # if the button is clicked
    # write a message
    st.write('Create a Histogram For the Car Sales Advertisements Dataset')

    # create histogram
    fig1 = px.histogram(car_data, x="odometer")

    # exibit interactive plotly graph
    st.plotly_chart(fig1, use_container_width=True)


# create a checkbox
build_scatterplot = st.checkbox('Create Scatter Plot')

if build_scatterplot:  # if box is checked
    # write a message
    st.write('Create a Scatter Plot For Odometer Column')

    # create a scatter plot
    fig2 = px.scatter(car_data, x="odometer", y="price")

    # exibit interactive plotly graph
    st.plotly_chart(fig2, use_container_width=True)
