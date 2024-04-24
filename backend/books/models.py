from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * self.get_discount())
    #AI markting model
    def get_discount(self):
        return 0.9
def __str__(self):
    return self.title

# Example books creation:
# Run these commands in Django shell to create example Book objects:
#   from your_app.models import Book
#   book1 = Book.objects.create(title='The Great Gatsby', author='F. Scott Fitzgerald', publication_date='1925-04-10', isbn='9780743273565', price=10.99)
#   book2 = Book.objects.create(title='To Kill a Mockingbird', author='Harper Lee', publication_date='1960-07-11', isbn='9780446310789', price=9.99)
#   book3 = Book.objects.create(title='1984', author='George Orwell', publication_date='1949-06-08', isbn='9780451524935', price=11.99)
#   book4 = Book(title='The Catcher in the Rye', author='J.D. Salinger', publication_date='1951-07-16', isbn='9780316769488', price=8.99)
#   book4.save()