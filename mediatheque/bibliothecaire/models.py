from django.db import models
from datetime import timedelta, date



class Media(models.Model):
    TYPE_CHOICES = [
        ('Livre', 'Livre'),
        ('DVD', 'DVD'),
        ('CD', 'CD'),
        ('JeuDePlateau', 'JeuDePlateau'),
    ]

    title = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    author_or_creator = models.CharField(max_length=200)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.type})"


class Emprunteur(models.Model):
    name = models.CharField(max_length=100)
    blocked = models.BooleanField(default=False)

    def can_borrow(self):
        
        if self.blocked:
            return False
        active_loans = Emprunt.objects.filter(emprunteur=self, returned=False).count()
        return active_loans < 3

    def __str__(self):
        return self.name


class Emprunt(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    emprunteur = models.ForeignKey(Emprunteur, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(default= date.today() + timedelta(days=7))
    returned = models.BooleanField(default=False)

    def is_overdue(self):
        
        return date.today() > self.due_date and not self.returned

    def save(self, *args, **kwargs):
        
        if self.media.type == 'JeuDePlateau':
            raise ValueError("Les jeux de plateau ne peuvent pas être empruntés.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.media.title} emprunté par {self.emprunteur.name}"
