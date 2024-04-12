from books.models import Book
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view

@api_view(["GET"])
def api_home (request, *args, **kwargs):
    response = {}
    book1 = Book.objects.all().order_by('id')[0]
    if book1:
        response = model_to_dict(book1, fields=['id', 'title', 'author', 'publication_date', 'isbn', 'price'])

    return Response(response)