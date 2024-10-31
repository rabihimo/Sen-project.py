import yfinance as yf
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Stock Price Evolution")

# Get the stock symbol from the user
symbol = st.text_input("Enter stock symbol :", "AAPL")

# Get the start and end dates for the data
start_date = st.date_input("Start date:", pd.to_datetime("2023-01-01"))
end_date = st.date_input("End date:", pd.to_datetime("today"))

# Download the stock data using yfinance
try:
    data = yf.download(symbol, start=start_date, end=end_date)
    if data.empty:
        st.error("No data found for the given symbol and dates.")
    else:
        # Create the candlestick chart
        fig = go.Figure(data=[go.Candlestick(x=data.index,
                                            open=data['Open'],
                                            high=data['High'],
                                            low=data['Low'],
                                            close=data['Close'])])

        fig.update_layout(title=f"{symbol} Stock Price",
                          xaxis_title="Date",
                          yaxis_title="Price")

        st.plotly_chart(fig)

        # Display the Open and Close prices in a table
        st.subheader("Open and Close Prices")
        st.dataframe(data[['Open', 'Close']])

except Exception as e:
    st.error(f"An error occurred: {e}")
