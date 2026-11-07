import json

with open("user.json", "r", encoding="utf-8") as fayl:
    foydalanuvchi = json.load(fayl)

print("Ism:", foydalanuvchi["ism"])
print("Yosh:", foydalanuvchi["yosh"])
print("Shahar:", foydalanuvchi["shahar"])
