#!/usr/bin/env python3

import os


#mise a jour du fichier inventaire.ini

print("Voici le contenu actuel du fichier inventaire:")

with open('inventaire.ini') as f:
    for line in f:
        print(line)

rep=input("Voulez-vous ajouter un noeud à l'inventaire ? (O/N) ")

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
#copie de clé ssh sur les nodes
#boucle sur l'ensemble des nodes du fichier inventaire
with open('inventaire.ini') as f:
     for line in f:
        os.system("ssh-copy-id -i ~/.ssh/id_ecdsa.pub administrateur@"+line)

#personnalisation de wordpress

#execution playbook
os.system("ansible-playbook -i inventaire.ini --user administrateur --become --ask-become-pass install-wordpress.yml")

