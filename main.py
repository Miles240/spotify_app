import requests
import json

url = "https://api.spotify.com/v1/playlists/37i9dQZEVXbMDoHDwVN2tF/tracks?limit=1"

payload = {}
headers = {
    'Authorization': f'Bearer BQBtFJLi3jMilbp54vtysHB18z-CYsPpJcM8V2c_3SIkd-zsKwXtBsswVCXOumEYg9URIPd6dzx08DMWMAOqX5ptnuBLwrM-xZe36reI2zJE1pzGC9o',
    'User-Agent': 'Apidog/1.0.0 (https://apidog.com)'
}

response = requests.get(url, headers=headers)

with open('file.json', 'w', encoding='utf-8') as file:
    json.dump(response.json(), file)


