import streamlit as st
import pandas as pd
import plotly.express as px

# Load your Excel data into a Pandas DataFrame
file_path = "GreenCell_Assignment.xlsx"
df = pd.read_excel(file_path)

# Calculate 10-day and 50-day moving averages

# Here 'MA' Means Moving Average
# Imagine tracking daily prices of something. A moving average helps smooth out short-term fluctuations.
# Instead of recalculating the average every day, it updates based on the prices of the last few days.
# This gives a clearer trend picture, helping us see beyond daily ups and downs in the data.
df['10_day_MA'] = df['Price'].rolling(window=10).mean()
df['50_day_MA'] = df['Price'].rolling(window=50).mean()

# Create an interactive line chart with Plotly Express
fig = px.line(df, x='Date', y=['Price', '10_day_MA', '50_day_MA'], title='Price Over Time', line_shape='linear', line_dash_sequence=['solid', 'solid', 'solid'], line_color=['white', 'blue', 'green'])

# Streamlit App
st.title("Assignment Analysis")

# Description
st.markdown("Welcome to my assignment analysis website. This page displays data and charts from my assignment.")

# Show the Excel data
st.subheader("Excel Data:")
st.write(df)

# Show the Plotly chart
st.subheader("Price Over Time Chart:")
st.plotly_chart(fig)

# Footer
st.markdown("Thanks for checking out my analysis! Feel free to explore the data and charts above.")
