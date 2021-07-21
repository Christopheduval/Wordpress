# Installation automatisée de Wordpress avec Ansible
***
Node-manager: Debian10  
version ansible 4  
node client: tests effectués sur ubuntu21  
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
La version 1 du projet concerne le déploiement de Wordpress sur des distributions Ubuntu Server 21. 
***

## Installation serveur Apache
création du role apache: installation d'un serveur apache2
 
***
## Installation php
création du role php: installation php en tant que processus FastCGI réalisée  
version php7.4 installée  

***
## Installation Mysql
création du role mysql: installation de la dernière version mysql

***
## Installation Wordpress
Le role wordpress permet d'effectuer les étapes suivantes:
  - création de l'hote virtuel pour Wordpress
  - téléchargement de la dernière version de Wordpress
  - création de la base de données wordpress
  - création de l'administrateur du site
  - création du fichier de configuration  
   
***

## Variables
Nom de la base de données wordpress: wordpress_db  
Nom de l'utilisateur wordpress: wordpress_user  
Mot de passe de l'utilisateur wordpress: wordpress_password

***
## Synthèse et amélioration du projet
Le script wordpress.py permet de:
  - de mettre à jour le fichier inventaire.ini
  - de mettre a jour le fichier /etc/hosts (nécessité d'avoir les droits sur ce fichier)
  - de vérifier que les noeud sont joignables
  - de copier une clé ssh sur les noeuds (il faut dans un 1er temps créer cette clé sur le node-manager avec la commande ssh-keygen -t ecdsa)
  - de personnaliser l'installation en saisissant les valeurs des variables suivantes:
    - wordpress_db: nom de la base de données wordpress
    - wordpress_user: identifiant de connexion à la base
    - wordpress_password: mot de passe de connexion
  - d'effectuer le déploiement sur les nodes ajoutés au fichier inventaire.ini

Les futures évolutions devront permettre:  
  - d'effectuer des déploiements sur d'autres distributions Linux
  - d'automatiser complètement l'installation d'un site Wordpress
