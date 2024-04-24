from rest_framework import generics

from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data.get('publication_date'))
        serializer.save()

book_list_create_view = BookListCreateAPIView.as_view()

class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

book_detail_view = BookDetailAPIView.as_view()

class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    lookup_field = 'pk'

    def perform_update(self, serializer):
        print('Book with id: ',self.kwargs['pk'],'updated!')
        return super().perform_update(serializer)
book_update_view = BookUpdateAPIView.as_view()
    
class BookDestroyAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    lookup_field = 'pk'

    def perform_destroy(self, instance):
        print(f'Book with id: ', instance.id, 'deleted!')
        return super().perform_destroy(instance)
    
book_destroy_view = BookDestroyAPIView.as_view()