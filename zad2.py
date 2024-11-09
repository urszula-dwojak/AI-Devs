import requests, os
from dotenv import dotenv_values

config = dotenv_values(".env")

# The API endpoint
url = config["URL"]
url_out = config["URL_OUT"]
# A GET request to the API
input_data = requests.get(url).text.strip().split('\n')
print(input_data)


answer = {
    "task": "POLIGON",
    "apikey": config["API_KEY"],
    "answer": input_data,
}

import json

print(json.dumps(answer))
converted_ans = json.dumps(answer)
response = requests.post(url=url_out, data=converted_ans)

print(response)
print(response.json())

