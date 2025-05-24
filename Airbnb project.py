import pandas as pd
df = pd.read_csv('airbnb_price_predictor.csv')
print(df)
print(df.info())
print(df.head())
print(df.describe())
print("Missing values:\n", df.isnull().sum())
df.dropna(inplace=True)
print("Duplicate rows:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
df['Listing ID'] = df['Listing ID'].str.strip()
df['Location'] = df['Location'].str.strip()
df['Location'] = df['Location'].str.title()
df = df[df['Listing ID'].str.match(r'LST\d{4}')]
df['Beds'] = pd.to_numeric(df['Beds'], errors='coerce')
df['Amenities Count'] = pd.to_numeric(df['Amenities Count'], errors='coerce')
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df['Price (USD)'] = pd.to_numeric(df['Price (USD)'], errors='coerce')
df.to_csv('cleaned_airbnb_data.csv', index=False)
print("Data cleaning complete. Cleaned file saved as 'cleaned_airbnb_data.csv'.")


