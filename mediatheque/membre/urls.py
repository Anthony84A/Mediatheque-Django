from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),  # Page d'accueil
    path('media/<str:type_media>/', views.liste_medias, name='liste_medias'),
]
