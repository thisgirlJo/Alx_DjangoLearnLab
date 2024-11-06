python manage.py shell
from bookshelf.models import Book
book = Book(title='1984', author='George Orwell', publication year= '1949')
book.save()