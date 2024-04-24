import requests

book_id = input('Enter the book id: ')

try:
    book_id = int(book_id)
except:
    book_id = None
    print(f'{book_id} not a valid id')
if book_id:
    endpoint = f'http://localhost:8000/api/books/{book_id}/delete'

get_response = requests.delete(endpoint)
print(get_response.status_code)