import requests

def fetch_gifs():
    url = "https://api.giphy.com/v1/gifs/trending"
    params = {
        "limit": 20,
        "rating": "g",
        "api_key": "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["data"]
    else:
        return None