from rest_framework import serializers
from .models import Listing

class ListingContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('id', 'name', 'description', 'price', 'rarity', 'condition',)
