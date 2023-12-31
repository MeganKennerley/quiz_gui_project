import requests

url = "https://opentdb.com/api.php"
params = {
    "amount": 10,
    "category": 9,
    "difficulty": "medium",
    "type": "boolean"
}
response = requests.get(url, params=params)
response.raise_for_status()
question_data = response.json()["results"]
