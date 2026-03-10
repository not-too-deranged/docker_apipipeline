import requests

def test_crypto_api():
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Berlin")
    assert r.status_code == 200
