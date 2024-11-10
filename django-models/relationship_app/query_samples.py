from .models import Author

filter = Author.objects.filter(name='George Orwell').values()
