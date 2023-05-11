# Utiliser l'image de base python
FROM python:3.9-slim-buster


# Définir le répertoire de travail de l'application
WORKDIR /app/backend

# Copier les fichiers de l'application dans l'image
COPY . .

# Installer les dépendances de l'application
RUN pip install --no-cache-dir -r requirements.txt


# Exposer le port utilisé par l'application
EXPOSE 8000

# Lancer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
