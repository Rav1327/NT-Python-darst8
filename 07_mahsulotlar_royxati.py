import csv

with open("products.csv", "r", encoding="utf-8", newline="") as fayl:
    mahsulotlar = list(csv.DictReader(fayl))

print("Barcha mahsulotlar:")
for mahsulot in mahsulotlar:
    print(mahsulot["nom"], mahsulot["narx"], mahsulot["miqdor"])

print("Umumiy qiymatlar:")
for mahsulot in mahsulotlar:
    umumiy = int(mahsulot["narx"]) * int(mahsulot["miqdor"])
    print(mahsulot["nom"], umumiy)

eng_qimmat = mahsulotlar[0]
for mahsulot in mahsulotlar:
    if int(mahsulot["narx"]) > int(eng_qimmat["narx"]):
        eng_qimmat = mahsulot

print("Eng qimmat mahsulot:", eng_qimmat["nom"], eng_qimmat["narx"])
