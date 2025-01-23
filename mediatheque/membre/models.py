from django.db import models

class Media(models.Model):
    TYPE_CHOICES = [
        ('livre', 'Livre'),
        ('cd', 'CD'),
        ('dvd', 'DVD'),
        ('jeu_de_plateau', 'Jeu de Plateau'),
    ]

    titre = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titre
