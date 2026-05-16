import pandas as pd

# Dataset
raw_data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Laptop', 'Mouse', None],
    'Revenue': [1200, 25, 300, 75, 1150, None, 150],
    'Cost': [800, 10, 200, 40, 850, 15, 100],
    'Date': ['2025-01-10', '2025-02-15', '2025-03-20',
             '2025-10-05', '2025-11-12', '2025-12-25',
             '2025-06-01']
}

# Create DataFrame
df = pd.DataFrame(raw_data)

print("Original DataFrame:\n")
print(df)

# 1. Handle Missing Values

# Fill missing Revenue with median
median_revenue = df['Revenue'].median()
df['Revenue'] = df['Revenue'].fillna(median_revenue)

# Fill missing Product with "Unknown"
df['Product'] = df['Product'].fillna("Unknown")

print("\nDataFrame After Handling Missing Values:\n")
print(df)

# 2. Feature Engineering

# Create Profit column
df['Profit'] = df['Revenue'] - df['Cost']

# Create Margin Percentage column
df['Margin_Percentage'] = (df['Profit'] / df['Revenue']) * 100

print("\nDataFrame After Feature Engineering:\n")
print(df)

# 3. Filtering

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Filter Q4 products (Oct, Nov, Dec) with Profit > 50
q4_filtered = df[
    (df['Date'].dt.quarter == 4) &
    (df['Profit'] > 50)
]

print("\nFiltered Q4 Products with Profit > 50:\n")
print(q4_filtered)