import requests
import json
import os
import sys
import time

token = input("Token: ")

while True:
    api = requests.get("https://discordapp.com/api/v6/invite/hwcVZQw")
    data = api.json()
    check = requests.get("https://discordapp.com/api/v6/guilds/" + data['guild']['id'], headers={"Authorization": token})
    stuff = check.json()
    requests.post("https://discordapp.com/api/v6/invite/hwcVZQw", headers={"Authorization": token})
    requests.delete("https://discordapp.com/api/v6/guiilds" + data['guild']['id'], headers={"Authorization": token})

    if stuff['code'] == 0:
        print("Successfully disabled")
        break

Nzg2MTg2MTQyNDAzNTI2Njc2.X9Cu5g.Yc_MKlGqpJFP-_dHg3_CYH0JZrM
