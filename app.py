from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

app = Flask(__name__)

# Step 1: Load Excel data into a Pandas DataFrame
df = pd.read_excel('GreenCell_Assignment.xlsx')

# Step 2: Create an interactive line chart with Plotly Express
# Plot the chart with date on the x-axis and values on the y-axis
fig = px.line(df, x='Date', y='Price', labels={'Date': 'Date', 'Price': 'Price'})


#Step 3: Calculate 10-day and 50-day moving averages

# Here 'MA' Means Moving Average
# Imagine tracking daily prices of something. A moving average helps smooth out short-term fluctuations.
# Instead of recalculating the average every day, it updates based on the prices of the last few days.
# This gives a clearer trend picture, helping us see beyond daily ups and downs in the data.

# Plot a 10-day moving average
df['10_day_ma'] = df['Price'].rolling(window=10).mean()
fig.add_trace(go.Scatter(x=df['Date'], y=df['10_day_ma'], mode='lines', name='10-day MA', line=dict(color='red')))

# Plot a 50-day moving average
df['50_day_ma'] = df['Price'].rolling(window=50).mean()
fig.add_trace(go.Scatter(x=df['Date'], y=df['50_day_ma'], mode='lines', name='50-day MA', line=dict(color='green')))

# Add the price line with custom color and name
fig.add_trace(go.Scatter(x=df['Date'], y=df['Price'], mode='lines', name='Price', line=dict(color='blue', width=2)))

# Configure the legend
fig.update_layout(legend=dict(
    orientation="h",  # horizontal legend
    yanchor="bottom",  # position of the legend
    y=1.02,  # adjust as needed
    xanchor="right",  # position of the legend
    x=1  # adjust as needed
))

# Step 4: Show the chart figure
# Convert the plot to HTML
plot_html = pio.to_html(fig, full_html=False)

@app.route('/')
def index():
    return render_template('index.html', df=df, plot_html=plot_html)

if __name__ == '__main__':
    app.run(debug=True)
