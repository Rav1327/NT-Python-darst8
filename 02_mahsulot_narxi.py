import json

with open("product.json", "r", encoding="utf-8") as fayl:
    mahsulot = json.load(fayl)

umumiy_qiymat = mahsulot["narx"] * mahsulot["miqdor"]

print("Mahsulot:", mahsulot["nom"])
print("Narx:", mahsulot["narx"])
print("Miqdor:", mahsulot["miqdor"])
print("Umumiy qiymat:", umumiy_qiymat)
