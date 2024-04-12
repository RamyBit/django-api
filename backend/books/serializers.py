from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    book_discount = serializers.SerializerMethodField(read_only= True)
    class Meta:
        model = Book
        fields =[
            'title',
            'author',
            'price',
            'sale_price',
            'book_discount'
        ]
    def get_book_discount(self,obj):
        if not isinstance(obj, Book):
            return None
        print(obj.id, obj.get_discount())
        return str(obj.get_discount())