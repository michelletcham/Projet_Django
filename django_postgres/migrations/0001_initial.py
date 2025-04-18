# Generated by Django 5.2 on 2025-04-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('ref', models.CharField(max_length=100, unique=True)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('geolocalisation', models.CharField(blank=True, max_length=255)),
                ('vector_search', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
