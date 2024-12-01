from django.db import models

#Data Models
#Author Model 
class Author(models.Model):
    name = models.CharField(max_length=100)
    
#Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)