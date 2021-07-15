#!/usr/bin/env python3

import os

#mise a jour du fichier inventaire.ini

#préparation des nodes

#execution playbook

os.system("ansible-playbook -i inventaire.ini --user user-ansible --become --ask-become-pass install-wordpress.yml")

