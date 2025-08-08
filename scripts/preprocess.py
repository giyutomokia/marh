import pandas as pd

def load_and_clean_data():
    # Load data
    trades = pd.read_csv("data/historical_data.csv")
    sentiment = pd.read_csv("data/fear_greed_index.csv")

    # Parse timestamp in historical data (fix format)
    trades['date'] = pd.to_datetime(trades['Timestamp IST'], format='%d-%m-%Y %H:%M', errors='coerce').dt.normalize()

    # Ensure classification date is datetime
    sentiment['date'] = pd.to_datetime(sentiment['date'], errors='coerce').dt.normalize()

    # Merge on date
    merged = pd.merge(trades, sentiment[['date', 'classification']], on='date', how='left')

    # Rename for clarity
    merged.rename(columns={'classification': 'sentiment', 'Closed PnL': 'closed_pnl'}, inplace=True)

    # Optional: Drop rows where date or sentiment is missing
    merged = merged.dropna(subset=['date', 'sentiment'])

    return merged[['date', 'closed_pnl', 'sentiment']]
