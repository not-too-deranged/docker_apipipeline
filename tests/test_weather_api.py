import requests

def test_crypto_api():
    r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    assert r.status_code == 200
