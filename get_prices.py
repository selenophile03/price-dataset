import pandas as pd
import os

def get_global_prices():
    url = "https://githubusercontent.com"
    print("📥 Fetching latest global price data...")
    df = pd.read_csv(url)
    
    df['date'] = pd.to_datetime(df['date'])
    latest_date = df['date'].max()
    
    latest_data = df[df['date'] == latest_date]
    clean_data = latest_data[['name', 'local_price', 'dollar_price', 'currency_code']].copy()
    clean_data.columns = ['Country', 'Local Price', 'Price in USD', 'Currency']
    
    return clean_data.sort_values(by='Price in USD')

if __name__ == "__main__":
    prices_df = get_global_prices()
    
    # Ensure a data directory exists
    os.makedirs("data", exist_ok=True)
    
    # Save the output inside the data directory
    prices_df.to_csv("data/global_prices.csv", index=False)
    print("✅ Success! Data saved to data/global_prices.csv")
