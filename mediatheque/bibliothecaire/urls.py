from django.urls import path
from . import views

urlpatterns = [
    path('media/', views.media_list, name='media_list'),
    path('media/add/', views.add_media, name='add_media'),
    path('emprunteur/', views.emprunteur_list, name='emprunteur_list'),
    path('emprunteur/add/', views.add_emprunteur, name='add_emprunteur'),
    path('emprunt/create/', views.create_emprunt, name='create_emprunt'),
    path('emprunt/return/<int:pk>/', views.return_emprunt, name='return_emprunt'),
]
