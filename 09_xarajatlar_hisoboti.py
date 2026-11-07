import csv

with open("expenses.csv", "r", encoding="utf-8", newline="") as fayl:
    xarajatlar = list(csv.DictReader(fayl))

yigindi = 0
eng_katta = xarajatlar[0]
for xarajat in xarajatlar:
    summa = int(xarajat["summa"])
    yigindi += summa
    if summa > int(eng_katta["summa"]):
        eng_katta = xarajat

print("Umumiy xarajat:", yigindi)
print("Eng katta xarajat:", eng_katta["nom"], eng_katta["summa"])
print("Xarajatlar soni:", len(xarajatlar))
