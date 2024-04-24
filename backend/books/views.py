from rest_framework import generics

from .models import Book
from .serializers import BookSerializer

class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

book_detail_view = BookDetailAPIView.as_view()