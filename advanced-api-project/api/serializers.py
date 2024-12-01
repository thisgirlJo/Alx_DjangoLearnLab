from rest_framework import serializers
from .models import Book, Author
from datetime import date

""" The BookSerializer serializes all fields of the Book Model
with a custom validation function that ensures the publication_year is never in the future
"""
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate(self, data):
        today = date.today()
        if (data['publication_year']) > today:
            raise serializers.ValidationError(
                "Incorrect Date Time"
            )
        return data

"""
The Author Serializer serializes the name field of the Authoe Model
"""
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name']