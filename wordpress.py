#!/usr/bin/env python3

import sys
from ansible import context
from ansible.module_utils._text import to_text
from ansible.cli.playbook import PlaybookCLI

# Read all the arguments from the cli
args = [to_text(a, errors='surrogate_or_strict') for a in sys.argv]

# Pass them to the playbook cli object
pb_cli = PlaybookCLI(args)

# Parse the arguments
pb_cli.parse()

# The context should now contain all of our parsed arguments
print(context.CLIARGS)
