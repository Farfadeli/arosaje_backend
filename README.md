### Arosaje_backend
Backend pour l'application Arosaje

## Démarrage de Django

Pour démarrer Django, suivez ces étapes :

1. Assurez-vous d'avoir Python installé sur votre système.
2. Mettez en place le repository github sur votre machine en local
3. Créer l'environnement virtuel
3. Une fois dans l'environnement virtuel positionner vous sur `django-web-app/merchex`
4. Exécutez `python manage.py runserver` pour démarrer le serveur de développement.
5. Pour retrouver les urls des crud se rendre dans `django-web-app/merchex/urls.py`

## Mise en place de la base de données Workbench

Pour configurer la base de données Workbench :

1. Créez la base de données :
   - Importez le fichier `scripts.sql` situé à la racine du projet dans Workbench.

2. Dans `django-web-app/merchex/settings.py`, modifiez ce qui suit :

```python
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

