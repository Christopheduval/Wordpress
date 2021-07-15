#!/usr/bin/env python3

import os

os.system("ansible-playbook -i inventaire.ini --user user-ansible --become --ask-become-pass install-wordpress.yml")

