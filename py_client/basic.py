import requests

# Defining the URL and pyload data
endpoint="http://localhost:11434"
url = "http://localhost:11434/api/generate"

payload ={
  "model": "llama2:7b",
  "prompt": "What color is the sky at different times of the day? Respond using JSON",
  "format": "json",
  "stream": False
}

# Sent GET request
get_response = requests.get(endpoint)
print(get_response.text)
# Sent POST request
post_response = requests.post(url, json=payload)

# Check the response
if post_response.status_code == 200:
    print("Response: ")
    print(post_response.json())
else:
    print("Error: ", post_response.status_code, post_response.text)