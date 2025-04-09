from django.contrib.gis.db import models

# Create your models here.

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    ref = models.CharField(max_length=100, unique=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    localisation = models.PointField(null=True, blank=True, srid=4326) 

    # Champ pour la recherche vectorielle (ex: embeddings IA)
    vector_search = models.JSONField(null=True, blank=True)  # Ex: [0.123, 0.456, ...]

    def __str__(self):
        return f"{self.nom} ({self.ref})"
