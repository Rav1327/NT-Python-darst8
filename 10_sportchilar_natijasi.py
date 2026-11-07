import csv

with open("sportchilar.csv", "r", encoding="utf-8", newline="") as fayl:
    sportchilar = list(csv.DictReader(fayl))

print("Barcha sportchilar:")
for sportchi in sportchilar:
    print(sportchi["ism"], sportchi["sport"], sportchi["ball"])

print("80 balldan yuqori natija olganlar:")
for sportchi in sportchilar:
    if int(sportchi["ball"]) > 80:
        print(sportchi["ism"], sportchi["sport"], sportchi["ball"])

eng_yuqori = sportchilar[0]
for sportchi in sportchilar:
    if int(sportchi["ball"]) > int(eng_yuqori["ball"]):
        eng_yuqori = sportchi

print("Eng yuqori ball:", eng_yuqori["ism"], eng_yuqori["sport"], eng_yuqori["ball"])
