FROM node:14.17.0-alpine3.13

# Définir le répertoire de travail de l'application
WORKDIR /app/frontend

COPY package.json .
COPY package-lock.json .

RUN npm install

COPY . .

# Installer les dépendances de l'application
RUN npm install build

# Exposer le port utilisé par l'application
EXPOSE 3000

# Lancer l'application
CMD ["npm", "start"]
