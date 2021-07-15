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

def creation_fichier_conf(wordpress_db,wordpress_user,wordpress_password):
    fichier_source = open('wordpress/files/modele-wp-config.php', 'r') 
    fichier_destination= open('wordpress/files/wp-config.php', 'w')

#on recopie les 24 premières lignes
    for i in range(24):
        txt = fichier_source.readline()
        fichier_destination.write(txt)
    
    txt = "define ( 'DB_NAME', 'wordpress' );"
    fichier_destination.write(txt)
    
    for i in range(4):
        txt = fichier_source.readline()
        fichier_destination.write('')
        
    txt = "define ( 'DB_NAME', 'wordpress' );"
    fichier_destination.write(txt)
 
    for i in range(4):
        txt = fichier_source.readline()
        fichier_destination.write('')
        
    txt = "define ( 'DB_NAME', 'wordpress' );"
    fichier_destination.write(txt)
    
    for i in range(67):
        txt = fichier_source.readline()
        fichier_destination.write(txt)
 


    fichier_source.close()
    fichier_destination.close()



test="yes"
creation_fichier_conf(test,test,test)

















