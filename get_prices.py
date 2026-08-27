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
    
    # Force creation of data directory in current workspace
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
    
    # Save the output file explicitly
    output_path = os.path.join(data_dir, "global_prices.csv")
    prices_df.to_csv(output_path, index=False)
    print(f"✅ Success! Data saved to: {output_path}")
