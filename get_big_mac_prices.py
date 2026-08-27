import pandas as pd

def get_global_prices():
    # Official raw URL from the Economist GitHub repository
    url = "https://githubusercontent.com"
    
    print("📥 Fetching latest global price data from GitHub...")
    df = pd.read_csv(url)
    
    # Convert date to datetime and grab the most recent data entry
    df['date'] = pd.to_datetime(df['date'])
    latest_date = df['date'].max()
    
    print(f"🗓️ Extracting records for the latest update: {latest_date.strftime('%Y-%m-%d')}")
    latest_data = df[df['date'] == latest_date]
    
    # Keep key columns: Country, Local Currency Price, Dollar Price, and Currency Code
    clean_data = latest_data[['name', 'local_price', 'dollar_price', 'currency_code']].copy()
    clean_data.columns = ['Country', 'Local Price', 'Price in USD', 'Currency']
    
    # Sort by cheapest to most expensive in USD
    return clean_data.sort_values(by='Price in USD')

if __name__ == "__main__":
    prices_df = get_global_prices()
    
    # Save to a local CSV file
    prices_df.to_csv("global_item_costs.csv", index=False)
    print("✅ Success! Data saved to 'global_item_costs.csv'.")
    
    # Preview the top 10 countries
    print("\n📋 Preview of Global Costs (Sorted by USD Value):")
    print(prices_df.head(10).to_string(index=False))
