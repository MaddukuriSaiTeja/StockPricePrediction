import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

def get_historical(quote):
    try:
        end = datetime.now()
        start = end - timedelta(days=2*365)  # Approximate 2 years
        data = yf.download(quote, start=start, end=end)

        if not data.empty:
            df = pd.DataFrame(data)
            df.to_csv(f'{quote}.csv')
            print(f"Data saved successfully for {quote}.")
        else:
            print(f"No data available for {quote}.")
    
    except Exception as e:
        print(f"Error retrieving data for {quote}: {e}")

# Example usage
get_historical("AAPL")  # Replace with any stock ticker