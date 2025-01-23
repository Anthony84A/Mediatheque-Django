from django.shortcuts import render
from .models import Media  # On importe le modèle Media

def accueil(request):
    # Récupération de tous les médias
    medias = Media.objects.all()
    return render(request, 'membre/accueil.html', {'medias': medias})


def liste_medias(request, type_media):
    # Récupération des médias en fonction du type
    medias = Media.objects.filter(type=type_media)
    return render(request, 'membre/liste_medias.html', {'medias': medias, 'type_media': type_media})
