import pandas as pd
import matplotlib.pyplot as plt
from scripts.preprocess import load_and_clean_data

# Load cleaned data
df = load_and_clean_data()

# Show a sample
print("✅ Sample data:")
print(df.head())

# Nulls
print("\n🧼 Null counts:\n", df.isnull().sum())

# Distribution
print("\n📊 Sentiment distribution:\n", df['sentiment'].value_counts())

# Compute average PnL per sentiment
avg_pnl = df.groupby('sentiment')['closed_pnl'].mean().sort_values()

# Plot
avg_pnl.plot(kind='bar')
plt.title('Average Trader PnL by Market Sentiment')
plt.xlabel('Market Sentiment')
plt.ylabel('Average Closed PnL')
plt.grid(True)
plt.tight_layout()
plt.show()
