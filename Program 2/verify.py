import requests

try:
    response = requests.get('http://localhost:5000')
    print("Communication successful:", response.text)
except Exception as e:
    print("Communication failed:", e)
