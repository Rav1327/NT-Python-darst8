import csv

with open("students.csv", "r", encoding="utf-8", newline="") as fayl:
    oquvchilar = list(csv.DictReader(fayl))

print("Barcha o'quvchilar:")
for oquvchi in oquvchilar:
    print(oquvchi["ism"])

print("20 yoshdan katta o'quvchilar:")
for oquvchi in oquvchilar:
    if int(oquvchi["yosh"]) > 20:
        print(oquvchi["ism"], oquvchi["yosh"])
