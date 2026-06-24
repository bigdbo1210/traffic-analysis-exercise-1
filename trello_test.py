import os
import requests

url = "https://api.trello.com/1/cards"

query = {
    "key": os.getenv("TRELLO_KEY"),
    "token": os.getenv("TRELLO_TOKEN"),
    "idList": os.getenv("TRELLO_LIST_ID"),
    "name": "Test Vulnerability Ticket",
    "desc": "Testing Trello integration from Python."
}

response = requests.post(url, params=query)

print("Status Code:", response.status_code)
print(response.text)