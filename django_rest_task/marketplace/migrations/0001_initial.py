# Generated by Django 4.2.7 on 2023-12-15 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketplaceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('description', models.TextField(blank=True, verbose_name='Descripcion')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, verbose_name='Precio')),
                ('location', models.CharField(blank=True, max_length=100, verbose_name='Domicilio')),
                ('property_type', models.CharField(blank=True, choices=[('House', 'House'), ('Apartment', 'Apartment')], max_length=50, verbose_name='Tipo de propiedad')),
                ('bedrooms', models.IntegerField(blank=True, verbose_name='Habitaciones')),
                ('bathrooms', models.IntegerField(blank=True, verbose_name='Banos')),
                ('square_feet', models.IntegerField(blank=True, verbose_name='Area del Inmueble')),
                ('available', models.BooleanField(blank=True, default=False, verbose_name='Disponibilidad')),
            ],
        ),
    ]