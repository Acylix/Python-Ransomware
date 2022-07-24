import requests

def send(message):
    requests.post(url="WEBHOOK", data={"content":message})
