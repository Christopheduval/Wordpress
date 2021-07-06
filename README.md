# Installation automatisée de Wordpress
***
Node-manager: Debian10  
version ansible 2.10  
node client: tests effectués sur ubuntu20  
[documentation utilisée](https://doc.ubuntu-fr.org/wordpress)  
***
## Table des matières
1. [Présentation](#Présentation)
2. [Installation serveur Apache](#Installation-serveur-Apache)
3. [Installation php](#Installation-php)
4. [Installation Mysql](#Installation-Mysql)
5. [Installation wordpress](#Installation-Wordpress)
6. [Synthèse et amélioration du projet](#Synthèse-et-amélioration-du-projet)
***
## Présentation
Ce projet a pour but d'automatiser l'installation d'un serveur Wordpress. Il est divisé en plusieurs étapes décrites dans la table des matières.  
Dans un 1er temps, le déploiement de Wordpress pourra s'effectuer sur des distributions Debian ou Ubuntu. 
***
## Installation serveur Apache
création du role apache  
installation apache2 réalisée  


problème apt-get à résoudre  
sécurisation du serveur à réaliser  
documentation du fonctionnement à détailler  
***
## Installation php
création du role php  
installation php en tant que processus FastCGI réalisée  
version php7.4 installée  

voir pour gérer le changement de version  
documention du fonctionnement à réaliser  
***
## Installation Mysql
création du role mysql  
installation réalisée  

sécurisation de la connexion à réaliser  
documentation du fonctionnement à réaliser  
***
## Installation Wordpress
création de l'hote virtuel pour Wordpress  
téléchargement de la dernière version de Wordpress  

création de la base de données wordpress  
création de l'administrateur du site  


fichier de configuration à réaliser  
prévoir test si la base est créée  
documentation à réaliser   
***

## Variables
Nom de la base de données wordpress: wordpress_db  
Nom de l'utilisateur wordpress: wordpress_user  
Mot de passe de l'utilisateur wordpress: wordpress_password

***
## Synthèse et amélioration du projet
création de module pour automatiser l'installation en fonction:  
1. du nom de domaine 
2. de l'emplacement du site wordpress  
