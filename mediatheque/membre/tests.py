from django.test import TestCase
from bibliothecaire.models import Media

class MembreTests(TestCase):
    def setUp(self):
        # Création de quelques médias
        Media.objects.create(title="Livre Disponible", type="Livre", author_or_creator="Auteur 1", available=True)
        Media.objects.create(title="Livre Non Disponible", type="Livre", author_or_creator="Auteur 2", available=False)

    def test_media_list_view(self):
        # Teste si la vue retourne uniquement les médias disponibles
        response = self.client.get('/membre/media/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Livre Disponible")
        self.assertNotContains(response, "Livre Non Disponible")
