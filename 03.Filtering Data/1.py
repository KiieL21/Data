import pandas as pd

df = pd.read_csv("laptop_price1.csv", encoding="utf-8")

# Cari semua baris yang mengandung "Apple" secara fuzzy
mask = df["Company"].astype(str).str.contains("Apple", case=False, na=False)
df[mask]

print(mask)

LL = df[df['Company']=="Apple"].value_counts('Company')
print(LL)