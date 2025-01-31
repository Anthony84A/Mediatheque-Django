# Mediatheque-Django

Devoir CEF programmer en orienté objet avec Python


## Prérequis

1. Installer Python 3.10 ou supérieur.
2. Installer Django
   
          ```bash 
             pip install django
          ```
Etapes :

3. Cloner le dépöt Github
   
           ```bash
          git clone <https://github.com/Anthony84A/Mediatheque-Django>
          cd <project_mediathèque>
          ```

4. Créer un environnement virtuel
   
       ```bash
              python -m venv venv
             source venv/bin/activate  # Sous Windows : venv\Scripts\activate
        ```

5. Installer les dépendances
   
        ```bash
              pip install -r requirements.txt
        ```

6. Configurer la base de données
   
   - Appliquez les migrations pour générer la base SQLite
     
            ```bash
           python manage.py migrate
             ```

7. Lancer le serveur:
    
       ```bash
              python manage.py runserver
        ```

   - Accéder aux applications via :
          - Bibliothécaires : http://127.0.0.1:8000/bibliothecaire/
          - Membres : http://127.0.0.1:8000/membre/


8. Créer des données de test:
    - Ajoutez des médias, des membres et des emprunts via l’interface de l’application bibliothecaire.
     
