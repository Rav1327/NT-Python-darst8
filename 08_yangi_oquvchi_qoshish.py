import csv


def qator_ol(sorov):
    qator = input(sorov)
    while qator.strip() == "":
        qator = input()
    return qator


ism = qator_ol("Ismni kiriting: ").strip()
yosh = qator_ol("Yoshni kiriting: ").strip()
kurs = qator_ol("Kursni kiriting: ").strip()

with open("students_8.csv", "r", encoding="utf-8", newline="") as fayl:
    matn = fayl.read()

if matn != "" and not matn.endswith("\n"):
    with open("students_8.csv", "a", encoding="utf-8", newline="") as fayl:
        fayl.write("\n")

with open("students_8.csv", "a", encoding="utf-8", newline="") as fayl:
    yozuvchi = csv.writer(fayl, lineterminator="\n")
    yozuvchi.writerow([ism, yosh, kurs])

print("Fayldagi barcha o'quvchilar:")
with open("students_8.csv", "r", encoding="utf-8", newline="") as fayl:
    for qator in csv.DictReader(fayl):
        print(qator["ism"], qator["yosh"], qator["kurs"])
