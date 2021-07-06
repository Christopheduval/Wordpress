#!/usr/bin/python
#-*- coding: utf-8 -*-

#from ansible.module_utils.basic import *

#def main():
#    module = AnsibleModule(
#           argument_spec={}
#         )

#creation du fichier wp-config.php a partir du fichier modele-wp-config.php
#les lignes 25,28,31 doivent être modifiées
#elles doivent indiquer les valeurs des variables wordpress_db, wordpress_user, worpress_password

#on ouvre les 2 fichiers

#si le fichier wp-config.php contient des valeurs, on efface son contenu


#on copie les lignes 1 à 24 du fichier modèle vers le fichier wp-config.php

#on copie la ligne 25 en ajoutant la valeur de wordpress_db

#on copie les lignes 26 à 27 du fichier modèle vers le fichier wp-config.php

#on copie la ligne 28 en ajoutant la valeur de wordpress_user

#on copie les lignes 29 à 30 du fichier modèle vers le fichier wp-config.php

#on copie la ligne 31 en ajoutant la valeur de wordpress_passwordi

#on copie les lignes 32 jusqu'à la fin du fichier modèle vers le fichier wp-config.php


#on ferme les 2 fichiers


with open('../wordpress/files/modele-wp-config.php', 'r') as file:
    for line in file: 
      print(line, end='')
    file.closed





