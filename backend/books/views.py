from rest_framework import generics

from .models import Book
from .serializers import BookSerializer

class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data.get('publication_date'))
        serializer.save()

book_create_view = BookCreateAPIView.as_view()

class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

book_detail_view = BookDetailAPIView.as_view()