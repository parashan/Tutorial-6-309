from rest_framework import serializers
from Store.models import Item
from django.contrib.auth.models import User

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['id', 'user', 'password']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'stock_count', 'price', 'picture']