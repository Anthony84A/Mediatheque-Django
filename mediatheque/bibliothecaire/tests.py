from django.test import TestCase
from .models import Media, Emprunteur, Emprunt

class BibliothecaireTests(TestCase):
    def setUp(self):
        # Création d'exemples de données
        self.media = Media.objects.create(title="Harry Potter", type="Livre", author_or_creator="J.K. Rowling", available=True)
        self.emprunteur = Emprunteur.objects.create(name="John Doe", blocked=False)

    def test_media_creation(self):
        # Vérifie que le média a bien été créé
        self.assertEqual(self.media.title, "Harry Potter")
        self.assertTrue(self.media.available)

    def test_emprunteur_can_borrow(self):
        # Vérifie que l'emprunteur peut emprunter
        self.assertTrue(self.emprunteur.can_borrow())

    def test_emprunt_creation(self):
        # Création d'un emprunt
        emprunt = Emprunt.objects.create(media=self.media, emprunteur=self.emprunteur)
        self.media.refresh_from_db()  # Recharge le média depuis la base
        self.assertFalse(self.media.available)  # Vérifie que le média n'est plus disponible
        self.assertEqual(emprunt.media, self.media)
        self.assertEqual(emprunt.emprunteur, self.emprunteur)

    def test_emprunteur_cannot_borrow_more_than_three_items(self):
        # Crée 3 emprunts pour cet emprunteur
        for i in range(3):
            media = Media.objects.create(title=f"Media {i+1}", type="Livre", author_or_creator="Author", available=True)
            Emprunt.objects.create(media=media, emprunteur=self.emprunteur)

        # Vérifie que l'emprunteur ne peut plus emprunter
        self.assertFalse(self.emprunteur.can_borrow())

    def test_media_cannot_be_borrowed_if_not_available(self):
        # Marquer le média comme non disponible
        self.media.available = False
        self.media.save()

        # Vérifie qu'on ne peut pas créer un emprunt
        with self.assertRaises(Exception):
            Emprunt.objects.create(media=self.media, emprunteur=self.emprunteur)
