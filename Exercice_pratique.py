import requests
import json

# Config pour l'API
key = "e0a1bf2c844edb9084efc764c089dd748676cc14"
url = "https://api.jcdecaux.com/vls/v3/stations/"
contract = "Creteil"


# Récupération du json par l'API
params = {
"apiKey": key, "contract": contract
}
response = requests.get(url, params=params)
stations = json.loads(response.text)


# Stats
mech_bikes_count = 0
elec_bikes_count = 0
bikes_sum = 0
mech_bikes_percent = 0
elec_bikes_percent = 0


# Traitement données
for station in stations:
    mech_bikes_count += station["totalStands"]["availabilities"]["mechanicalBikes"]
    elec_bikes_count += station["totalStands"]["availabilities"]["electricalBikes"]

bikes_sum = mech_bikes_count + elec_bikes_count


# Calcul des pourcentages
mech_bikes_percent = mech_bikes_count * 100 / bikes_sum
elec_bikes_percent = elec_bikes_count * 100 / bikes_sum


# Affichage des données
print(f"Contract : {contract}\nPourcentage de vélos mécaniques  : {mech_bikes_percent}%\nPourcentage de vélos électriques : {elec_bikes_percent}%")