import requests

endpoint = 'http://localhost:8000/api/books/'
post_respone = requests.post(endpoint, {'title': 'newbook', 'author': 'newAuthor','publication_date': '1925-04-10', 'price':'0'})
print(post_respone)
print(post_respone.json())