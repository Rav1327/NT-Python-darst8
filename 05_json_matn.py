import json

talaba = {
    "ism": "Sardor",
    "yosh": 20,
    "kurs": 2
}

json_matn = json.dumps(talaba)
print(json_matn)

yangi_talaba = json.loads(json_matn)
print(yangi_talaba["ism"])
