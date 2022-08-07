import requests

def send(message):
    requests.post(url="https://discord.com/api/webhooks/1000508473156567120/wS9UX9_ptmwFdrksuQLCsiT542Po1EqoswKzvIXSyPVyZH-ETmiqqfdBxvyM_RGptESf", data={"content":message})

def better_round(number, decimals):
    multiplier = 10 ** decimals
    return int(number * multiplier) / multiplier
