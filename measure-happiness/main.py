import string

import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("happy.csv")


def for_label(value):
    return string.capwords(value.replace(" ", "_"))


def for_table(value):
    return value.replace(" ", "_").lower()


if __name__ == '__main__':
    st.title("In Search of Happiness")
    col_names = df.columns
    column_labels = [for_label(i) for i in list(col_names)]
    x_axis = for_table(st.selectbox(label="Select the data for the x-axis", options=column_labels,
                                    key='x_axis'))
    y_axis = for_table(st.selectbox(label="Select the data for the y-axis", options=column_labels, key='y_axis'))
    st.subheader(f"{for_label(x_axis)} and {for_label(y_axis)}")
    figure = px.scatter(x=df[x_axis], y=df[y_axis], labels={"x": for_label(x_axis), "y": for_label(y_axis)})
    st.plotly_chart(figure)
