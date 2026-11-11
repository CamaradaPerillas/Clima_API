import requests

información = requests.get(
"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Madrid/2026-11-10/2026-11-10?unitGroup=metric&elements=tempmax,tempmin"
)

información_d = información.json()

print(información)
print(información_d)
for a in información_d["days"]:
	print(f"Región: {información_d["address"]}\nTemperatura máxima: {a["tempmax"]}\nTemperatura mínima: {a["tempmin"]}")

