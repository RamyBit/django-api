import requests

endpoint = 'http://localhost:8000/api/books/'

get_response = requests.get(endpoint)
print(get_response)
print(get_response.json())