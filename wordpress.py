#!/usr/bin/env python3

import os

#fonction pour effacer l'écran
def EffaceEcran():
    os.system("clear")

#mise a jour du fichier inventaire.ini
EffaceEcran()
print("Voici le contenu actuel du fichier inventaire:\n")

with open('inventaire.ini') as f:
    for line in f:
        print(line)


rep=input("Voulez-vous ajouter un noeud à l'inventaire ? (O/N) ")
EffaceEcran()

while rep != "N":
    host=input("Entrer le nom du noeud: ")
    ip=input("Entrer son adresse ip: ")
    with open('inventaire.ini', 'a') as f1:
        s1 = str(host)
        f1.write(s1+'\n')
    with open('/etc/hosts', 'a') as f2:
        s2 = str (ip)
        f2.write(s2+" "+s1+"\n")
    rep=input("Voulez-vous ajouter un autre noeud à l'inventaire ? (O/N) ")


#préparation des nodes

#verification de la connexion
print("test de ping")
print("")
with open('inventaire.ini') as f:
    for line in f:
        os.system("ping -c 3 -q "+line) 

#copie de clé ssh sur les nodes
#boucle sur l'ensemble des nodes du fichier inventaire
EffaceEcran()
print("copie de la clé publique ssh sur les nodes")

with open('inventaire.ini') as f:
    for line in f:
        os.system("ssh-copy-id -i ~/.ssh/id_ecdsa.pub administrateur@"+line)

#personnalisation de wordpress
os.system("cp wordpress/files/modele-wp-config.php wordpress/files/wp-config.php")

wordpress_db = "wordpress"
wordpress_user = "wordpress"
wordpress_password
import os

#fonction pour effacer l'écran
def EffaceEcran():
    os.system("clear")

def Menu():
    print("1. Afficher le contenu du fichier inventaire")
    print("2. Effacer le contenu du fichier inventaire")
    print("3. Ajouter des noeuds à l'inventaire")
    print("4. Vérifier la connexion aux nodes")
    print("5. Copie des clés ssh sur les nodes")
    print("6. Personnaliser l'installation de Wordpress")
    print("7. Lancer le déploiement de Wordpress")
    print("8. Quitter le programme\n")
    choix=int(input("Quel est votre choix ?"))
       
    if choix==1:
        AfficheInventaire()
    elif choix==2:
        EffaceInventaire()
    elif choix==3:
        AjoutInventaire()
    elif choix==4:
        TestConnexion()
    elif choix==5:
        CopieCle()
    elif choix==6:
        CopieCle()
    elif choix==7:
        PersonnaliseWordpress()        
    elif choix==8:
        return


#Affichage du fichier inventaire.ini
def AfficheInventaire():
    EffaceEcran()
    print("Voici le contenu actuel du fichier inventaire:\n")
    with open('inventaire.ini') as f:
        for line in f:
            print(line)
    print("Tapez sur la touche Entrée pour retourner au menu principal")
    input()
    Menu()

#Effacement du fichier inventaire.ini
def EffaceInventaire():
    EffaceEcran()
    with open('inventaire.ini', 'w') as f:
        f.write("")
    print("Tapez sur la touche Entrée pour retourner au menu principal")
    input()
    Menu()

#Ajouter des noeuds au fichier inventaire.ini
def AjoutInventaire():
    EffaceEcran()
    rep = "O"
    while rep != "N":
        host=input("Entrer le nom du noeud: ")
        ip=input("Entrer son adresse ip: ")
        with open('inventaire.ini', 'a') as f1:
            s1 = str(host)
            f1.write(s1+'\n')
        with open('/etc/hosts', 'a') as f2:
            s2 = str (ip)
            f2.write(s2+" "+s1+"\n")
        rep=input("Voulez-vous ajouter un autre noeud à l'inventaire ? (O/N) ")
    print("Tapez sur la touche Entrée pour retourner au menu principal")
    input()
    Menu()


#verification de la connexion aux nodes
def TestConnexion():
    EffaceEcran()
    print("test de ping")
    print("")
    with open('inventaire.ini') as f:
        for line in f:
            os.system("ping -c 3 -q "+line)
    print("Tapez sur la touche Entrée pour retourner au menu principal")
    input()
    Menu()

#copie de clé ssh sur les nodes
#boucle sur l'ensemble des nodes du fichier inventaire
def CopieCle():
    EffaceEcran()
    print("copie de la clé publique ssh sur les nodes")
    with open('inventaire.ini') as f:
        for line in f:
            os.system("ssh-copy-id -i ~/.ssh/id_ecdsa.pub administrateur@"+line)
    print("Tapez sur la touche Entrée pour retourner au menu principal")
    input()
    Menu()

#personnalisation de wordpress
def PersonnaliseWordpress():
    os.system("cp wordpress/files/modele-wp-config.php wordpress/files/wp-config.php")
    
    wordpress_db = "wordpress"
    wordpress_user = "wordpress"
    wordpress_password = "wordpress"

    EffaceEcran()
    reponse=input("Souhaitez-vous personnaliser l'installation de wordpress ? (O/N) (Par défaut, la base de donnée créée sera wordpress avec un utilisateur et un mot de passe identique) : ")
    if reponse == "O":
        wordpress_db=input("saisir le nom de la base de données: ")
        wordpress_user=input("saisir le nom de l'utilisateur: ")
        wordpress_password=input("saisir le mot de passe: ")

    with open('wordpress/defaults/main.yml', 'w') as f:
        f.write('---\n')
        f.write('wordpress_db: "'+wordpress_db+'"\n')
        f.write('wordpress_user: "'+wordpress_user+'"\n')
        f.write('wordpress_password: "'+wordpress_password+'"')

    #mise à jour du fichier wp-config.php
    os.system("cp wordpress/files/wp-config-debut.php wordpress/files/wp-config.php")
    with open('wordpress/files/wp-config.php', 'a') as f:
        f.write("define( 'DB_NAME', '"+wordpress_db+"' );\n")
        f.write("define( 'DB_USER', '"+wordpress_user+"' );\n")
        f.write("define( 'DB_PASSWORD', '"+wordpress_password+"' );\n")
    os.system("cat wordpress/files/wp-config-fin.php >> wordpress/files/wp-config.php")
    print("Tapez sur la touche Entrée pour retourner au menu principal")
    input()
    Menu()

#execution playbook
def ExecutePlaybook():
    os.system("ansible-playbook -i inventaire.ini --user administrateur --become --ask-become-pass install-wordpress.yml")
    
    

Menu()



