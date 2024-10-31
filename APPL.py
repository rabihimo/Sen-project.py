import yfinance as yf
import streamlit as st
import pandas as pd

st.title('Stock Price Evolution')

# Input for stock symbol
symbol = st.text_input("Enter Stock Symbol:", "AAPL")

# Input for date range
start_date = st.date_input("Start Date", pd.to_datetime('2023-01-01'))
end_date = st.date_input("End Date", pd.to_datetime('today'))


# Fetch data
try:
    data = yf.download(symbol, start=start_date, end=end_date)

    if data.empty:
        st.error(f"No data found for symbol '{symbol}' within the specified date range.")
    else:
        # Display the data
        st.write(f"Data for {symbol} from {start_date} to {end_date}")
        st.dataframe(data[['Open', 'Close']])  # Show only 'Open' and 'Close' columns


        # Plotting
        st.line_chart(data[['Open', 'Close']])

except Exception as e:
    st.error(f"An error occurred: {e}")
