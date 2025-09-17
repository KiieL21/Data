import pandas as pd

# Buka file CSV sebagai teks mentah
with open("laptop_price1.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

expected_cols = len(lines[0].strip().split(","))  # jumlah kolom dari header
print(f"Jumlah kolom seharusnya: {expected_cols}")

# Cek baris yang punya Apple + jumlah kolomnya tidak sesuai
problem_rows = []
for i, line in enumerate(lines[1:], start=2):  # mulai dari baris ke-2 (karena header baris 1)
    if "Apple" in line:
        col_count = len(line.strip().split(","))
        if col_count != expected_cols:
            problem_rows.append((i, col_count, line.strip()))

# Tampilkan hasil
if problem_rows:
    print(f"Ditemukan {len(problem_rows)} baris Apple yang kolomnya bermasalah:\n")
    for row_num, col_count, content in problem_rows:
        print(f"Baris {row_num} → {col_count} kolom\n{content}\n")
else:
    print("Semua baris Apple jumlah kolomnya sesuai.")



df = pd.read_csv("laptop_price1.csv", encoding="utf-8")

# Cari semua baris yang mengandung "Apple" secara fuzzy
mask = df["Company"].astype(str).str.contains("Apple", case=False, na=False)
df[mask]
