import requests

def test_nasa_api():
    r = requests.get("https://api.nasa.gov/planetary/apod?api_key=54HEklHMM96BTb1gY16hUdOImJB3sZq3m0j9s9Vm")
    assert r.status_code == 200
