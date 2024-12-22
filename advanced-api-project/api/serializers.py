from rest_framework import serializers
from .models import Book, Author
from datetime import date

""" The BookSerializer serializes all fields of the Book Model
with a custom validation function that ensures the publication_year is never in the future
"""

"""
The Author Serializer serializes the name field of the Authoe Model
"""
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

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
    author = AuthorSerializer(read_only=True)

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        