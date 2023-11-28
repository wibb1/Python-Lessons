import pandas as pd
import streamlit as st
import plotly.express as px
from backend import get_data

WEATHER_IMAGES = {
    "Clear": "images/clear.png",
    "Clouds": 'images/cloud.png',
    "Rain": 'images/rain.png',
    "Snow": "snow.png"
}
ABBREVIATIONS = {
    "Imperial": "F", "Metric": "C", "Kelvin": "K"
}

if __name__ == '__main__':
    st.title("Weather Forcast for the Next Days")
    place = st.text_input(label="Place:")
    days = st.slider(label="Select data to view", min_value=1, max_value=5, step=1,
                     help="Select a number of forecasted days")
    units = st.selectbox(label='Select your units', options=['Imperial', 'Metric', 'Kelvin'])
    view_data = st.selectbox(label="Select data to view", options=["Temperature", "Sky"])
    if place:
        try:
            data = get_data(place, days, units.lower())
            if view_data == "Temperature":
                st.header(f"Temperature for the next {days} days in {place}")
                temperatures = [dict['main']['temp'] for dict in data]
                dates = [dict['dt_txt'] for dict in data]
                figure = px.line(x=dates, y=temperatures,
                                 labels={"x": "Date", "y": f"Temperature ({ABBREVIATIONS[units]})"})
                st.plotly_chart(figure)
            elif view_data == 'Sky':
                st.header("Sky")
                sky_conditions = [dict['weather'][0]['main'] for dict in data]
                sky_images = [WEATHER_IMAGES[condition] for condition in sky_conditions]
                st.image(sky_images, width=85)
            else:
                raise ValueError('Unknown data to view selected.')
        except KeyError:
            st.error("The place entered was not found")
