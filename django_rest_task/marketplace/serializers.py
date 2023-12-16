from rest_framework import serializers
from .models import MarketplaceModel

class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketplaceModel
        fields = ['id', 'title', 'description', 'price', 'location', 
                  'property_type', 'bedrooms', 'bathrooms', 'square_feet', 'available']