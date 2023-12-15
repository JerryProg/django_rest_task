from django.contrib import admin
from .models import MarketplaceModel

# Register your models here.
class MarketPlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'location', 
                    'property_type', 'bedrooms', 'bathrooms', 'square_feet', 'available')


admin.site.register(MarketplaceModel, MarketPlaceAdmin)