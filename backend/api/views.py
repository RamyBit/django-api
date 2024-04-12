from books.serializers import BookSerializer
from books.models import Book
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view

@api_view(["GET"])
def api_home (request, *args, **kwargs):
    response = {}
    book1_instance = Book.objects.all().order_by('id')[0]
    if book1_instance:
       response = BookSerializer(book1_instance).data

    return Response(response)