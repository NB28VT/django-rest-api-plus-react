from rest_framework import serializers
from .models import Todo

# Inherit from model serializer
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        # that's a tuple:
        fields = (
            "id",
            "title",
            "description"
        )
        model = Todo
