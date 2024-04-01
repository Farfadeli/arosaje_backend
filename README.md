# arosaje_backend
Back for arosaje app



# Mise en place de la BDD Workbench
Créer la BDD:
importer le scripts.sql qui se trouvent à la racine du projet dans workbench.

Dans django-web-app/merchex/settings.py

modifier:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nom-de-la-dd',
        'USER': 'nom-utilisateur-de-connexion',
        'PASSWORD': 'mot-de-passe-user',
        'HOST': 'localhost',  # Ou l'adresse IP de votre serveur MySQL
        'PORT': '3306',  # Par défaut, le port MySQL est 3306
    }
}


La base de donnée et la connexion à django est terminée.

