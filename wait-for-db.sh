#!/bin/bash

# Attendre que la base de données soit prête
echo "Waiting for database..."
while ! nc -z db 5432; do
  sleep 1
done
echo "Database is ready!"

# Lancer les migrations
python manage.py migrate

# Démarrer l'application
python manage.py runserver 0.0.0.0:8000