import requests

def fetch_external_api():
    url = "https://economia.awesomeapi.com.br/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch external API")