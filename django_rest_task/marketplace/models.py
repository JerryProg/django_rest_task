from django.db import models

# Create your models here.
class MarketplaceModel(models.Model):
    PROPERTY_TYPE = (
        ('House', 'House'),
        ('Apartment', 'Apartment'),
    )

    title = models.CharField("Titulo", max_length=100)
    description = models.TextField("Descripcion", blank=True)
    price = models.DecimalField("Precio", max_digits=10, decimal_places=2, blank=True)
    location = models.CharField("Domicilio", max_length=100, blank=True)
    property_type = models.CharField("Tipo de propiedad", max_length=50, choices=PROPERTY_TYPE, blank=True)
    bedrooms = models.IntegerField("Habitaciones", blank=True)
    bathrooms = models.IntegerField("Banos", blank=True)
    square_feet = models.IntegerField("Area del Inmueble", blank=True)
    available = models.BooleanField("Disponibilidad", default=False, blank=True)

    class Meta:
        db_table = "marketplace"

    def __str__(self):
        return f"{self.title}" 
    