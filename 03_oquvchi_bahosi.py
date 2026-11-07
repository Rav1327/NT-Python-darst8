import json

with open("student.json", "r", encoding="utf-8") as fayl:
    oquvchi = json.load(fayl)

oquvchi["ball"] = 95

with open("student.json", "w", encoding="utf-8") as fayl:
    json.dump(oquvchi, fayl, indent=4, ensure_ascii=False)

print("Ball 95 ga o'zgartirildi va faylga saqlandi")
print(oquvchi)
