```python
from bookshelf.models import Book
book = Book.objects.all()[0]
book.delete
```