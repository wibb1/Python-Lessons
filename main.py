import os

import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

DIARY_LOCATION = "diary"

analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores("I am in love with you!")
print(scores)


def get_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


def get_diary(file_paths):
    diary_loc = {}
    for filepath in file_paths:
        with open(filepath) as file:
            day = file.read()
            index = filepath.find("\\")
            diary_loc[filepath[index + 1:-4]] = day
    return diary_loc


def analyze_diary(diary_loc):
    analysis = {}
    for page in diary_loc:
        analysis[page] = analyzer.polarity_scores(diary_loc[page])
    return analysis


def get_data_type(data_type, data):
    values = []
    for date in data:
        values.append(data[date][data_type])
    return values


if __name__ == '__main__':
    filepaths = get_file_paths(DIARY_LOCATION)
    diary = get_diary(filepaths)
    results = analyze_diary(diary)
    dates = results.keys()

    st.title("Diary Tone")
    st.header("Positivity")
    positives = get_data_type("pos", results)
    figure1 = px.line(x=dates, y=positives, labels={"x": "Date", "y": "Polarity"})
    st.plotly_chart(figure1)

    st.header("Negativity")
    negatives = get_data_type("neg", results)
    figure1 = px.line(x=dates, y=negatives, labels={"x": "Date", "y": "Polarity"})
    st.plotly_chart(figure1)
