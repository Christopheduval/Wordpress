#!/usr/bin/env python3

import os

#mise a jour du fichier inventaire.ini

#préparation des nodes
os.system("ssh-copy-id -i ~/.ssh/id_ecdsa.pub administrateur@srvubuntu")
os.system("ssh-copy-id -i ~/.ssh/id_ecdsa.pub administrateur@http")


#os.system("ansible-playbook -i inventaire.ini -m user -a 'name=user-ansible' --user administrateur --ask-pass --become --ask-become-pass all")

#personnalisation de wordpress

#execution playbook

os.system("ansible-playbook -i inventaire.ini --user administrateur --become --ask-become-pass install-wordpress.yml")

