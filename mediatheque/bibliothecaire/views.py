from django.shortcuts import render, redirect, get_object_or_404
from .models import Media, Emprunteur, Emprunt
from django.http import HttpResponse
from django.shortcuts import render




def accueil_bibliothecaire(request):
    return render(request, 'bibliothecaire/accueil.html')


# Liste des médias
def media_list(request):
    medias = Media.objects.all()
    return render(request, 'bibliothecaire/media_list.html', {'medias': medias})

# Ajouter un média
def add_media(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        media_type = request.POST.get('type')
        author_or_creator = request.POST.get('author_or_creator')
        Media.objects.create(title=title, type=media_type, author_or_creator=author_or_creator, available=True)
        return redirect('media_list')
    return render(request, 'bibliothecaire/add_media.html')

# Liste des emprunteurs
def emprunteur_list(request):
    emprunteurs = Emprunteur.objects.all()
    return render(request, 'bibliothecaire/emprunteur_list.html', {'emprunteurs': emprunteurs})

# Ajouter un emprunteur
def add_emprunteur(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Emprunteur.objects.create(name=name, blocked=False)
        return redirect('emprunteur_list')
    return render(request, 'bibliothecaire/add_emprunteur.html')

# Créer un emprunt
def create_emprunt(request):
    if request.method == 'POST':
        media_id = request.POST.get('media_id')
        emprunteur_id = request.POST.get('emprunteur_id')
        media = get_object_or_404(Media, id=media_id, available=True)
        emprunteur = get_object_or_404(Emprunteur, id=emprunteur_id)

        # Vérifier les contraintes métier
        if not emprunteur.can_borrow():
            return HttpResponse('Emprunteur bloqué ou limite atteinte.', status=400)

        # Créer l'emprunt
        Emprunt.objects.create(media=media, emprunteur=emprunteur)
        media.available = False
        media.save()
        return redirect('media_list')

    medias = Media.objects.filter(available=True)
    emprunteurs = Emprunteur.objects.all()
    return render(request, 'bibliothecaire/create_emprunt.html', {'medias': medias, 'emprunteurs': emprunteurs})

# Retourner un emprunt
def return_emprunt(request, pk):
    emprunt = get_object_or_404(Emprunt, pk=pk)
    emprunt.returned = True
    emprunt.media.available = True
    emprunt.media.save()
    emprunt.save()
    return redirect('media_list')
