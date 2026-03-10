import requests

def test_nasa_api():
    r = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    assert r.status_code == 200
