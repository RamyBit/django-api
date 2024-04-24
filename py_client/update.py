import requests
book_id = input('Enter the book id: ')

try:
    book_id = int(book_id)
except:
    book_id = None
    print(f'{book_id} not a valid id')
if book_id:
    endpoint = f'http://localhost:8000/api/books/{book_id}/update'

payload = {'title': 'updatedbook', 'author': 'updatedAuthor','publication_date': '1925-04-10', 'price':'0'}
get_response = requests.put(endpoint, payload)
print(get_response)
print(get_response.json())