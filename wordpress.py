#!/usr/bin/env python3

import os


#mise a jour du fichier inventaire.ini

#préparation des nodes
#copie de clé ssh sur les nodes
#boucle sur l'ensemble des nodes du fichier inventaire
with open('inventaire.ini') as f:
    for line in f:
        os.system("ssh-copy-id -i ~/.ssh/id_ecdsa.pub administrateur@"+line)

#personnalisation de wordpress

#execution playbook

os.system("ansible-playbook -i inventaire.ini --user administrateur --become --ask-become-pass install-wordpress.yml")

