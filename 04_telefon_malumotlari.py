import json


def qator_ol(sorov):
    qator = input(sorov)
    while qator.strip() == "":
        qator = input()
    return qator


with open("phone.json", "r", encoding="utf-8") as fayl:
    telefon = json.load(fayl)

print("Model:", telefon["model"])

yangi_narx = int(qator_ol("Yangi narxni kiriting: "))
telefon["narx"] = yangi_narx

with open("phone.json", "w", encoding="utf-8") as fayl:
    json.dump(telefon, fayl, indent=4, ensure_ascii=False)

print("Narx yangilandi va faylga saqlandi")
print(telefon)
